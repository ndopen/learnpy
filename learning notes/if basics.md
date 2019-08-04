### 1. 布尔值的用武之地
>　条件语句让人选择性的执行对应的语句快，使用if条件判断语句，返回布尔值来确定执行的代码块；
> `Python老手Laura Creighton指出的，这种差别类似于“有些东西”和“没有东西”的差别，而不是真和假的差别。`
```python
# 在if语句中以下都为假值
False   None   0   ""   ()   []   {}

>>> True
True
>>> False
False
>>> True == 1
True
>>> False == 1
False
>>> True + False +42
43
```
- 布尔值转换
> 而bool 与list 、str 和tuple 一样，可用来转换其他的值。
```python
>>> bool('I think, therefore I am')
True
>>> bool(42)
True
>>> bool('')
False
>>> bool(0)
False
>>> bool([])
False
```

### 2. 简单的if else
>if 语句，让您有条件的执行代码.
```python
# if语句
name = input('your is name?')
if name.endswith('cock'):
    print('hello, {}' .format(name))

# if else语句
name = input('your is name?')
if name.endswith('cock'):
    print('hello, {}' .format(name))
else:
    print('print else' + name)

# 一种特殊的表达式`条件表达式`
status = "friend" if name.endswith("Gumby") else "stranger"
```

### 2. elif子句
> 检查多个语句使用elif，elif语句时if else的缩写
```python
name = input('your is name?')
if name.endswith('cock'):
    print('hello, {}' .format(name))
elif name.endswith('lisi'):
    print('hello,' + name)
else:
    print(name)
```

### 3. 代码块嵌套
> if 语句内嵌套if语句
```python
name = input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Gumby')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Gumby')
    else:
        print('Hello, Gumby')
else:
    print('Hello, stranger')
```

### 4. 复杂的条件表达
>　if　语句的全部知识　条件判读本身

- 比较运算符 
>　if条件判断的基础运算符，比较运算符

|表|式描述|
|-|-|
|x == y|x 等于y|
|x <  y|x 小于y|
|x >  y|x 大于y|
|x >= y|x 大于或等于y|
|x <= y|x 小于或等于y|
|x != y|x 不等于y|
|x is y|x 和y 是同一个对象|
|x is not y|	x 和y 是不同的对象|
|x in y|	x 是容器（如序列）y 的成员|
|x not in y|	x 不是容器（如序列）y 的成员|

- 相等运算符
> `==` 确定两个对象是否相等
```python
>>> 'str' == 'str'
True
>>> 'str' == 'int'
False
```

- 相等运算符
> is 用来比较两个对象是否是同一个对象（==　比较是否相等），而is not检查两个对象是否不相同,不要将is 用于数和字符串等不可变的基本值。
```python
>>> x = y = [1,2,3]
>>> z = [1,2,3]
>>> x == z
True
>>> x is z
False
>>> x is not z
True
>>> x is y
True
```

- 成员资格运算符
>　检查一个对象是否包含在另一个对象中
```python
name = input('What is your name?')
if 's' in name:
    print('Your name contains the letter "s".')
else:
    print('Your name does not contain the letter "s".')
```

- 字符串和序列的比较
> 字符串是根据字符的字母排列顺序进行比较的
```python
>>> 'alpha' < 'beta'
True
>>> 'alpha' < 'alpha'
False
>>> 'alpha' < 'Alpha'
False
>>> 'alpha' < 'betastr'
True
>>> 'clpha' < 'betastr'
False
```
> 要获悉字母的顺序值，可使用函数ord 。这个函数的作用与函数chr 相反;
```python
# 区分字母大小写
>>> 'a'.lower() == 'A'.lower()
True
>>> 'a' == 'A'
False
```
> 序列值之间的比较计算同样是根据字符的字母排序进行比较
```python
>>> [1,2] < [2,1]
True
>>> [2,1] < [1,2]
False
>>> ['a','b'] < ['b','a']
True
>>> ['a', ['b', 'c']] < ['b', ['c','b']]
True
>>> ['b', ['b', 'c']] < ['a', ['c','b']]
```

- 布尔运算符
> 布尔运算符也称之为'逻辑运算符',通常检查一个条件是否为真时很容易理解表达，但可能需要检查判断多个条件；

> 检查多个条件时使用`and` `or` `not`这三个运算符进行判断
```python
# and接受两个值，当两个是真值是返回True,否则返回False
rule80 = 80
rule120 = 120
rule160 = 160
pace = input('当前数据：')

if rule80 <= pace and rule120 >= pace:
    print('平安驾驶,当前速度：{}'.format(pace))

elif rule80 > pace or rule120 <= pace and rule160 > pace:
    print('危险驾驶,当前速度：{}'.format(pace))

elif rule160 <= pace:
    print('严重超速,当前速度：{}'.format(pace))
else:
    print('数据错误')
```

- assert断言
> 如果知道必须满足特定条件，程序才能正确地运行，可在程序中添加assert 语句充当检查点，这很有帮助
```python
>>> age = 10
>>> assert 0 < age < 100
>>> age = -1
>>> assert 0 < age < 100
Traceback (most recent call last):
   File "<stdin>", line 1, in ?
AssertionError
```