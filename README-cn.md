[English](https://github.com/wuranxu/oson/blob/master/README.md)


### 介绍

  这是一个为将Python对象转换成JSON对象的库，目前支持原生类对象和flask-sqlalchemy的model对象。
 
#### 安装

```shell script
pip3 install oson
```

### 常规用法
```python
from datetime import datetime
import oson

class Student(object):
    name = 'Tom'
    age = 23
    update_at = datetime.now()
    __private = "don't see it"

s = Student()
print(oson.dumps(s))
```

### 高级用法
```python
from datetime import datetime
import oson

class Student(object):
    name = 'Tom'
    age = 23
    update_at = datetime.now()
    __private = "don't see it"

oson.set_config(time_format='%Y-%m-%d %H:%M:%S', date_format='%Y-%m-%d %H:%M:%S', private=False)

s = Student()
print(oson.dumps(s))
```

### 配置

  高级用法的配置，目前有3个参数。可以用```oson.set_config```方法进行设置。

- private

  是否导出私有成员变量，默认不导出。
  
- time_format

  设置datetime时间格式, 默认是```2019-12-28 15:00:00```

- date_format

  设置日期格式, 默认是```2019-12-28```
  
### 其他

- 反序列化功能暂时没有实现
- dump和load方法还没支持，不过考虑到场景可能用的比较少