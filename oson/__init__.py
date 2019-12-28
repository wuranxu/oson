__version__ = '0.0.1'

from oson.pson import Pson


def dumps(data, **kw):
    """
    encode python object to json
    :param data:
    :param kw:
    :return:
    """
    return Pson.dumps(data, **kw)


def loads(data, obj=None, **kw):
    """
    decode data to python object use default json
    :param data:
    :param obj:
    :param kw:
    :return:
    """
    return Pson.loads(data, obj, **kw)


def set_config(time_format='%Y-%m-%d %H:%M:%S', date_format='%Y-%m-%d %H:%M:%S', private=False):
    """
    set encode config
    :param time_format:
    :param date_format:
    :param private:
    :return:
    """
    Pson.private = private
    Pson.time_format = time_format
    Pson.date_format = date_format
