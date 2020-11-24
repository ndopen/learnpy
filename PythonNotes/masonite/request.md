> 当服务器首次启动时，将对 Request 类进行初始化，并在每个请求上对其进行修改。这意味着 Request 类充当单例，并且不会在每个请求上都重新初始化。

# request 辅助函数
```
from masonite.request import Request

def show(self, request:Request):
    db = request.input('name')

# 使用request不用指定函数行参
def show(self)
    db = request.input('name')
```
    + nete: 在获取输入数据时，任何 HTTP 方法 (GET，POST，PUT 等) 之间没有区别。它们都可以通过此 .input() 方法检索的，因此，如果请求是 GET 或 POST ，则无需进行区分。

# input
- 获取request所有输入
- 以字典形式返回该请求的所有可用请求输入变量
- 您可以通过将 False 传入方法或显式指定它们来排除它们
```python
return request.all(internal_variables = False) # {'user': 'Joe', 'status': '1'}
```

# inout Cleaning
- clean 输入数据将清除 HTML 标记和其他安全隐患。如果您期望获取 JSON 字符串之类的东西，则可能会导致不想要的返回值。
- has 要检查是否存在某些请求输入数据
```python
    """method
        Flash or true
    """
    request.input('name', clean = Flash)
    request.has('Remember')
```

# 获取字典输入
```python
    """
    Payload: 
    "user": {
        "id": 1,
        "addresses": [
            {"id": 1, 'street': "A Street"},
            {"id": 2, 'street': "B Street"}
        ] 
    }
    """
    request.input('payload')['user']['address]
    request.input('payload.user.address')
    request.input('payload.user.*.id')
```

# only获取特定的参数
```python
# GET: /dashboard?firstname=Joe&lastname=Mancuso&active=1

def show(self, request: Request):
    return request.only('firstname', 'active') # {'firstname': 'Joe', 'active': '1'}
```
# without 排除输入数据中一组特定的参数
```python
# GET: /dashboard?firstname=Joe&lastname=Mancuso&active=1

    def show(self)
        return request.without('lastname') # {'firstname': 'Joe', 'active': '1'}
```
# URL获取参数值
```python
ROUTE:/blog/@id/update
#GET :/blog/id/update
    def update(self, request:Request)
        request.param('id')
```
# JSON Payloads
- Masonite 将检测到传入请求是 JSON 请求，并将 JSON 转换为字典，然后将其加载到有效负载请求输入中。
- 然后，我们可以使用常规的 input() 方法在控制器中获取此输入

# cookies
- encrypt 选择是否加密
- expires cookie过期时间
```python
def show(self, request: Request):
    return request.cookie('key', 'value', encrypt=False, expires="5 minutes")
```

# httponly
- 作为安全措施，所有 cookie 都将自动使用 HttpOnly 标志进行设置，Javascript 代码无法使用这些 cookie。您可以关闭此功能：

# 路由
```python
    Get('/dashboard').name('dashboard') # 调用路由name方法

    request.route('dashboard.user', {'user': 1})# 可传入字典 列表

```

# Get('/dashboard').name('dashboard')
```python
# GET /dashboard/user/1
def show(self, request: Request):
    request.contains('/dashboard/*/1') #== True
```
# 获取当前链接
```python
return request.path #== /dashboard/user
```
