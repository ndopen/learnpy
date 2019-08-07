# 循环语句
> 循环执行指定代码快，直到满足条件时循环停止，for循环及while循环；
```
>>> while x <= 10:
...     print(x)
...     x += 1
... 
1
2
3
4
5
6
7
8
9
10
```

### 1. while循环
> while循环语句，当条件表达式为Ture时循环停止;
```python
name =''
while not name or name.isspace():
    name = input('please enter your name:')
print('hello {}'.format(name))
```

### 2. for循环
> for循环可对可迭代的数据序列进行遍历循环,`如果能用for,就不要使用while．`
```python
language = ['zh', 'en', 'de', 'jp']
for lang in language:
    print(lang)
```
> range()内置获取范围值的函数，
```python
>>> range(10)
range(0, 10)
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> for number in range(1, 10):
...  print(number)
```
- 迭代字典
> 
```python
d = {'x':1, 'y':2, 'z':3}
for key in d:
    print(key, 'vlues', d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key,value)
```

- 一些迭代的工具
> python 提供了一些有用的迭代序列的函数，其中一些位于itertools模块中;

1. 并行迭代
> 两种方法实现并行迭代序列，一种是建立循环索引,一种是使用函数zip将两个数据序列按照位置关系进行缝合(两个序列不一样取至短)，形成一个新的元组序列;
```python
name = ['cock', 'zhangsan', 'lisi']
age = [23, 19, 48]
for i in range(len(name)):
    print('{}同志的年龄是：{}'.format(name[i],age[i]))

for itme in zip(name, age):
    # print(names, '同志的年龄是：', ages)
    print('{}同志的年龄是：{}'.format(itme[0],itme[1]))
```

2. 迭代时获取索引
> 函数让你能够迭代索引-值对，其中的索引是自动提供的。
```python

for index, string in enumerate(names):
    if 'cock' in string:
        # names[index] = '[censored]'
        print(names[index], index)
```

3. 反向迭代和排序后再迭代
> reversed 和sorted实现排序迭代
```python
s = ['5', '1', '9', '3']
d = {'d':2, 'c':7, 'i':0}
print(' '.join(reversed('hello')))
print(sorted(s, key=str.lower))
print(list(reversed(s)))

# Print Output:
o l l e h
['A', 'c', 'D', 'E']
['3', '9', '1', '5']
```

### 3. break 语句
> 停止程序当前循环进入下一次循环，或停止循环
```python
# 找出小于100的最大平方值
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
# Print Output:
81
-{
    n: 81,
    root: 9,
    sqrt: -{
        py/function: "math.sqrt"
    }
}
```

### 4. continue
> contiune语句结束当前循环剩余部分，但不结束循环;


### 5. while true/berak(这种方法很实用)
> 使用　while true/berak成例，循环条件为false时避免执行过多的代码；
```python
#　while为true,执行循环代码，用户无任何输入，代码继续循环，word为空值
word = 'hello'
while word:
    word = input('please enter a word:')
    print('the word was', word)

# while 始终为true,执行循环内代码,if not word判断用户输入情况，如not word为true时执行break结束循环
while True:
    word = input('please enter a word:')
    if not word: 
        break
    print(word)
```

### 6. 循环中使用else语句
> 在循环中使用else语句,循环遇到break时执行else语句,无论是在for 循环还是while 循环中，都可使用continue 、break 和else 子句。
```python
# while循环 else执行控制
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print('while else')
# Print Output:
while else
-{
    n: 82,
    root: 9.055385138137417,
    sqrt: -{
        py/function: "math.sqrt"
    }
}
```
### 7. 简单的列表推导
> 列表推导是一种从其他列表创建列表的方式
```python
>>> [x * x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x * x for x in range(10) if x % 3 == 0]
[0, 9, 36, 81]
>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```
> 将名字的首字母相同的男孩和女孩配对
```python
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
print(letterGirls)
```

> 可使用花括号来执行字典推导
```python
>>> squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
>>> squares
{0: '0 squared is 0', 1: '1 squared is 1', 2: '2 squared is 4', 3: '3 squared is 9', 4: '4 squared is 16', 5: '5 squared is 25', 6: '6 squared is 36', 7: '7 squared is 49', 8: '8 squared is 64', 9: '9 squared is 81'}
```

### 8. pass dle exec
- pass
> pass 什么也不做，临时代码留空不报错;
```python
for target_list in expression_list:
    pass
else:
    pass
```

- del
> 删除不是用的对象（删除值及对象名称）
```python
>>> x = ["Hello", "world"]
>>> y = x
>>> y[1] = "Python"
>>> x
['Hello', 'Python']
>>> del x
>>> y
['Hello', 'Python']
```
- 使用exec 和eval 执行字符串及计算其结果
```python
# 不理解　后续ｇｏｏｇｌ
pass
```
