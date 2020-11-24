### 创建controller carft
- parameter 
    + create cxactController `--e ro --exact`
    + create resourceController `--r ro --resource` 
```
craft controller Dashboard
```

# definition controller method
- all controller include self
```python
    def show(self):
        pass
```

### 容器解析
- 所有控制器方法和构造函数都由容器解析，因此您还可以通过将它们指定为方法中的参数来从容器中检索其他对象
    + 通过方法参数索引对象
```python
    def show(self, request:Request)
        pass
```
    + 通过类的构造函数指定
```python
    from masonite.request import Request
    from app.Dashboard import *
    class DashboardController:
        def __init__(self,request:Request):
            self.request = request

        def show(self):
            dashboard = Dashboard.find(self.request('id)) 
```
- NOTE:需要注意的是，与其他框架不同，我们不必将路由参数指定为控制器方法中的参数。我们可以使用如 request.param('key') 类似方法获取参数。

### 返回JSON
- 返回Dict，然后将其解析
- 放回list
- 返回模型实例或者数据合集
```python
    class Dashboard:
        def __init__(self):
            pass

        def show(self, request:Request):
            # 返回dict list 模型实例
            return {'key':'value'}
            return ['key', 'value']
            return User.find(request.id(1))
```
- 放回分页响应及数据集合(两种返回的数据结构不一样) 
    + paginate()
    + paginator() 

### 传递路由参数
- 您可以将路由参数与解析代码一起传递
- request的param方法获取路由参数
```python
    from masonite.request import Request
    from masonite.view import View
    ...

    def show(self, request: Request, view: View):
        return User.find(request.param('user_id'))

    def show(self, user_id, view: View):
    return User.find(user_id)
```






