# 在谈print(),import()
> 发现print中的几个隐藏特性，使用`logging`模块写日志比print更合适

### 1. 打印多个参数
＞　print()打印可打印多条参数内容，多条参数与逗号相隔，可指定`sep` `end`参数指定打印的分隔符号．
```python
>>> name = 'Cock'
>>> salutation = 'Mr.'
>>> greetiong = 'hello,'
>>> print(greetiong,salutation,name)
hello, Mr. Cock
# 自定义多个参数之间的分隔符
>>> print(greetiong,salutation,name, sep="_")
hello,_Mr._Cock
# 自定义打印参数的结尾符
>>> print(greetiong,salutation,name, end='!')
hello, Mr. Cock!
```

### 2. import 导入模块时重命名
> 当导入两个模块时都包含相同的名称的函数时，可使用`as`模块命名
```python
>>> import math as foobar
>>> foobar.sqrt(4)
2.0
>>> from math import sqrt as foo
>>> foo(4)
2.0
```
### 3. 赋值魔法
> 同时给多个变量赋值，使用这种方式还可以赋值交换，这种方式称为`序列解包`
```python
# 同时赋值，安装位置
x, y, z = 1, 2, 3,
# 赋值交换
x, y = y, x

# Print Output:
-{
    x: 2,
    y: 1,
    z: 3
}
```
- 系列解包
> 一个数据系列可快速赋值，按位赋值，如左右两侧变量名与数据不对等时程序将报错，可是使用`*`来收集多余的数据到列表中；
```python
>>> values = 1, 2, 3
>>> values
(1, 2, 3)
>>> x, y, z =values
>>> y
2
＃ 使用*号收集多余数据
>>> values = 1, 2, 3, 4
>>> values
(1, 2, 3, 4)
>>> a, *b, c = values
>>> b
[2, 3]
>>> a
1
>>> c
4
```
- 将返回值的函数及方法解析到对应的变量中
> 示例中使用popitem随机删除字典中的一个项，并同时赋值给对应的变量;
```python
>>> scoundrel = {'name':'cock', 'girlfriend':'Marion'}
>>> key, value = scoundrel.popitem()
>>> key
'girlfriend'
>>> value
'Marion'
```

### 4. 链式赋值
> 链式赋值是一种快捷赋值方式，将多个变量关联到一个值上，（链式赋值的只是关联到父变量的值上，并非copy）
```python
# 链式赋值
k = t = ['a', 'b']
z = 'a'
v = 'b'
# Print Output:
-{
    k: -[
        "a",
        "b"
    ],
    t: -{
        py/id: 0
    },
    v: "b",
    z: "a"
}
```

### 5. 赋值增强
> 进行标准运算表达式时，可简化运算表达式及赋值方式，适用于`标准运算符`及其他运算符
```python
>>> x = 2
>>> x += 1
>>> x *= 2
>>> x
6
>>> fnord = 'foo'
>>> fnord += 'bar'
>>> fnord *= 2
>>> fnord
'foobarfoobar'
```

### 6. 理解`缩进`的代码块
> 代码块不是一种语句，代码块表示的是一组语句（表达式）,如判断语句if，循环语句等；
> 使用制表符Tab来缩进代码块，设置一次Tab为４个空格
```python
if condition:
    pass
else:
    pass
```