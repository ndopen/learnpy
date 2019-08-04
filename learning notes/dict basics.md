# dict字典用途
> 字典需要一系列值组合成数据结构，并通过编号来访问各个值，这种数据结构称为映射（mapping).


1. 使用两个列表获取列表中的对应的值
```python
# 使用列表方式获取对应列表中的值
>>> names = ['chuxiong', 'kunming', 'dali']

>>> numbers = ['0871', '0878', '0823']

>>> numbers[names.index('chuxiong')]
'0871'
```
</hr>

### 2. 创建字典 
> 字典由键 及其相应的值 组成，这种键-值对称为项 （item）,键必须是独一无二的．
```python
itemes = {'name':'gumby', 'age':42}
```
</hr>

### 3. dict函数
> dict函数将其他键－值结构的数据创建为字典
```python
>>> items = [('name', 'gumby'), ('age', 42)]
>>> d= dict(items)
>>> d
{'name': 'gumby', 'age': 42}
>>> d['name']
'gumby'

#使用关键子实参调用 
>>> d = dict(name='cock', age=42)
>>> d
{'name': 'cock', 'age': 42}

```
### 4. 字典基本操作
- len(itme) 返回字典中项(键－值)的数量
- dictname[key] 返回字典中与kye关联的值
- dictname[key] = 'china' 将值映射到键上
- del dictname[key] 删除指定的键－值(不带参数将删除整个字典)

```python
>>> dictname = {'name':'cock', 'age':18}
>>> len(dictname)
2
>>> dictname['age'] = 20
>>> dictname
{'name': 'cock', 'age': 20}
>>> del dictname['name']
>>> dictname
{'age': 20}
```
### ５．fromat_map字符串功能用于字典
> 很有用的替换方法
```python
template = '''<html>
<head>
    <title>{title}</title>
    </head>
    <body>
    <h1>{title}</h1>
    <p>{test}</p>
    </body>
</html>
'''
title = '创建和使用字典'
test = '字典由键 及其相应的值 组成，这种键-值对称为项 （item）。在前面的示例中，键为名字，而值为电话号码。每个键与其值之间都用冒号（: ）分隔，项之间用逗号分隔，而整个字典放在花括号内。空字典（没有任何项）用两个花括号表示，类似于下面这样：{} 。'

data = dict([('title', title), ('test', test)])
print(template.format_map(data))
```

### 6. 字典方法
- clear
> 方法clear()清楚所有itmel,返回None
```python
>>> d = {}
>>> d['name'] = 'cockroach'
>>> d['age'] = 342
>>> d
{'name': 'cockroach', 'age': 342}
>>> clear_itmle
>>> clear_itmle = d.clear()
>>> d
{}
>>> print(clear_itmle)
None
```

- copy复制字典
> copy()浅复制，使用deepcopy模块实现深复制；

```python
#三种实现copy的方法，（修改copy副本内容父副本跟着修改）
x = {'name':'admin', 'qiuxing' : ['qx1', 'qx2', 'qx3']}
y = x.copy()
z = x
y['name'] = 'cock'
y['qiuxing'].remove('qx2')
print(z)
#输出内容
Print Output:
{'name': 'cock', 'qiuxing': ['qx1', 'qx3']}
-{
    x: -{
        name: "cock",
        qiuxing: +[2 items]
    },
    y: -{
        name: "admin",
        qiuxing: +{1 items}
    },
    z: -{
        name: "cock",
        qiuxing: +{1 items}
    }
}
```

- deepcopy深度复制字典
> deepcopy()深度复制父副本为一个新副本，修改内容不影响父副本
```python
from copy import deepcopy
x = {'name':'admin', 'qiuxing' : ['qx1', 'qx2', 'qx3']}
y = x.copy()
z = deepcopy(x)
x['name'] = 'cock'
ｚ['qiuxing'].remove('qx2')
print(z)
#输出内容
Print Output:
{'name': 'admin', 'qiuxing': ['qx1', 'qx3']}
-{
    x: -{
        name: "cock",
        qiuxing: -[
            "qx1",
            "qx2",
            "qx3"
        ]
    },
    y: -{
        name: "admin",
        qiuxing: -{
            py/id: 0
        }
    },
    z: -{
        name: "admin",
        qiuxing: -[
            "qx1",
            "qx3"
        ]
    }
}
```

- fromkeys
> 创建一个新字典，指定键名，每个键对应的值为None(可以自定义值)
```python
itme_dict = dict()
p = itme_dict.fromkeys(['name', 'age'], '(N/O)')
d = dict.fromkeys(['china', 'japan'])

# Print Output:
-{
    d: -{
        china: null,
        japan: null
    },
    itme_dict: {},
    p: -{
        age: "(N/O)",
        name: "(N/O)"
    }
}
```
- get 调用字典项值
> 使用get调用没有定义的项，不会报错，返回指定的内容（默认返回None)
```python
itme_dict = dict()
itme_dict['name'] = 'cock'
print(itme_dict.get('age', 'N/A'))
# Print Output:
N/A
-{
    itme_dict: -{
        name: "cock"
    }
}
```

- items 获取字典中的键－值
> itmes 返回键－值列表，返回值属于＂字典视图＂的特殊类型
```python
>>> d = {'1':'q', '2':'w'}
>>> d.items()
dict_items([('1', 'q'), ('2', 'w')])
```

- keys() 获取字典键
> keys返回＂字典视图＂，包含字典键
```python
>>> d = {'1':'q', '2':'w'}
>>> d.keys()
dict_keys(['1', '2'])
```

- values()返回字典值
> 返回一个包含字典值的＂字典视图＂
```python
>>> d
{'1': 'q', '2': 'w', '3': 'z', '4': 'w'}
>>> d.values()
dict_values(['q', 'w', 'z', 'w'])
```

- pop
> pop() 删除指定键－值，并获取该值
```python
>>> d.pop('4')
'w'
```

- popitem
> popitme()随机删除字典项,并返回删除的键－值
```python
>>> d.popitem()
('3', 'z')
>>> d
{'1': 'q', '2': 'w'}
```

- setdefault
> setdefault()与get类似，获取指定键的值，当没有定义指定的items时，添加该键到字典中，可自定义值（默认值为None）.
```python
>>> d
{'1': 'q', '2': 'w'}
>>> d.setdefault('3', 'N/A')
'N/A'
>>> d
{'1': 'q', '2': 'w', '3': 'N/A'}
>>> d.setdefault('4')
>>> d
{'1': 'q', '2': 'w', '3': 'N/A', '4': None}
```

- update
> update()使用一个字典的项更新另一个字典，包含相同的键时替换该键-值,没有该项时添加；可使用＂类型构造函数＂那样调用update
```python
>>> d
{'1': 'q', '2': 'w', '3': 'N/A', '4': None}
>>> x = {'4':'t', '5':'o'}
>>> d.update(x)
>>> d
{'1': 'q', '2': 'w', '3': 'N/A', '4': 't', '5': 'o'}
```