<!--
 * @Author: your name
 * @Date: 2019-11-14 22:52:38
 * @LastEditTime: 2019-11-14 23:09:14
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /learnpy/PythonNotes/function base.md
 -->
# 目录
* [1.callable函数](#1.callable)
* [2.createFuntion](#2.CreateFuntion)

# 1.callable
> 函数是结构化编程的核心知识，函数在执行特定化任务的时候会返回值，但并非所有定义的函数将一定会返回值,要判定函数是否可用使用内置函数callable
```python
>>> import math
>>> x = 1
>>> y = math.sqrt
>>> callable(x)
False
>>> callable(y)
True
```

# 2.CreateFuntion
> 使用def关键字定义函数，并向函数传递值；
- 在定义函数时创建的参数为`形参`，在调用函数时定义的参数为`实参`;
```python
# CreateFuntion
def hello(name):
    return 'hello' + name
hello('cock')
```

