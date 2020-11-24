# 路由支持列表

# 路由組
```python
    RouteGroup([
        Get('/', 'PostController@show'),
        Get('/@id', 'PostController@single'),
        Get('/@id/update', 'PostController@update'),
        Get('/@id/delete', 'PostController@delete'),
        Get('/@id/store', 'PostController@store'),
    ],
    middleware=('auth',),
    domain='subdomain',
    prefix='/posts',
    name='post',
    ),
```
# 路由组嵌套

# View Routes

# 重定向路由 redirect
```python
ROUTES = [
    Redirect('/old/route', '/new/route', status=302, methods=['GET', 'POST'])
]
```

# 匹配路由
    - 使用 Match 方法

# 路由命名
    - 使用 name() 方法

# 路由中间件
    - 中间件是在请求之前或之后执行类，任务或动作的好方法。

# 深目录控制器
```python
Get('/dashboard', 'users.DashboardController@show')
```

# 全局控制器
- 使用 /指定全局路由的完整路径访问
- 导入类使用
```python
Get('/dashboard', '/thirdparty.package.users.DashboardController@show')
```
# 路由参数
- 该方法在requset中创建一个字典
- 可以在controller中使用 param()函数获取
```python
Get('/dashboard/@id', 'Controller@show')

request.param('id')
```

# 路由可选参数
- 使用? 替换 @
- 使用 default()函数设定默认值
```python
Get('/dashboard/user/?option', 'Controller@show')
```

# 路由编译器
- 默认 `int` `string`
- 可注册服务提供者，使用正则表达式定义

```python
Get('/@id:year', 'PostController@single').name('single'),

"""A RouteCompilerProvider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.routes import Route


class RouteCompilerProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, route: Route):
        """Boots services required by the container."""
        route.compile('year', r'([0-9]{4})')

```

# 子路由
- 子路由默认不开启
- 在调用domain中，可使用 '*' 通配符匹配所有子域名
- 需要在 `wsgi = False` 服务提供者中添加 `request.activate_subdomains()` 激活
```python
# joseph.example.com/dashboard  example.com/dashboard 
Get().domain('joseph').route('/dashboard', 'Controller@show')

wsgi = False
...
def boot(self, request: Request):
    request.activate_subdomains()
```



