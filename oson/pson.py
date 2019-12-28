"""
For Python object Marshal/Unmarshal to Python Object
"""
__author__ = 'woody'

import json
from datetime import date
from datetime import datetime

# default properties in class
DEFAULT_PROPERTIES = ['__dict__', '__doc__', '__module__', '__weakref__']


class Pson(object):
    time_format = '%Y-%m-%d %H:%M:%S'
    date_format = '%Y-%m-%d %H:%M:%S'
    private = False

    @staticmethod
    def set_config(time_format='%Y-%m-%d %H:%M:%S', date_format='%Y-%m-%d %H:%M:%S', private=False):
        Pson.private = private
        Pson.time_format = time_format
        Pson.date_format = date_format

    @staticmethod
    def dumps(data, **kwargs):
        cfg = dict(default=Pson.default, private=Pson.private, date_format=Pson.date_format,
                   time_format=Pson.time_format)
        # create metaclass to change
        meta_cls = type('JsonCustomEncoder', (json.JSONEncoder,), cfg)
        return json.dumps(data, cls=meta_cls, **kwargs)

    @staticmethod
    def loads(data, obj=None, **kw):
        """
        support non-object data only  #TODO
        :param data:
        :param obj:
        :param kw:
        :return:
        """
        # if obj is None or not isinstance(obj, object):
        return json.loads(data, **kw)

    @staticmethod
    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime(self.time_format)
        elif isinstance(field, date):
            return field.strftime(self.date_format)
        elif isinstance(field, object):
            return Pson.parse(field, self.private)
        else:
            return json.JSONEncoder.default(self, field)

    @staticmethod
    def parse_orm(obj, columns):
        return {c.name: getattr(obj, c.name) for c in columns}

    @staticmethod
    def parse(data, private=False):
        result = dict()
        table = getattr(data, '__table__')
        if table is not None and isinstance(table, object):
            columns = getattr(table, 'columns')
            if columns is not None:
                return Pson.parse_orm(data, columns)

        for x in dir(data):
            if not hasattr(getattr(data, x), '__call__') and x not in DEFAULT_PROPERTIES:
                key = x
                if x.startswith("_"):
                    if not private:
                        continue
                    key = x.replace("_{}".format(data.__class__.__name__), '')
                value = getattr(data, x)
                result[key] = value
        return result
