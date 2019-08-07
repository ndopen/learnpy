# 目录
* [callable函数](http://#callable)
* [createFuntion](http://#CreateFuntion)

# callable
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

# CreateFuntion
> 使用def关键字定义函数
```python
# CreateFuntion
def hello(name):
    return 'hello' + name
hello('cock')
```

