[中文说明](https://github.com/wuranxu/oson/blob/master/README-cn.md)

### Desc

  It's a library for python users to encode python objects to json.Use it just like use default json library.
  
#### Install

```shell script
pip3 install oson
```

### Unusual Usage
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

### More
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

### Config

- private

  if you need to encode private column, set it True.
  
- time_format

  use it to transfer time from datetime to time string

- date_format

  just like 『time_format』
  
### GOOD LUCK!