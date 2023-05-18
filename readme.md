# django

py --version 
Python 3.11.1

django-admin --version 
4.2.1

## 下载
```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django
```

## 创建项目
```python
django-admin startproject project
```

## 创建一个 app 
```python
python manage.py startapp app
```


### 注册 app
project/settings
```python
# app名称.apps.app名称Config

INSTALLED_APPS = [
    ...,
    'app.apps.AppConfig',
]
```

## 编写 url
project/urls
```python
from app import views

urlpatterns = [
    path('index/', views.index),
]
```

## 编写视图函数
app/views
```python
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('index 函数')
```

## 启动项目
如果首次启动
```python
python manage.py migrate
```
```python
python manage.py runserver
```

## 使用模板和静态文件
app/views.py
```python
def user_list(request):
    return render(request, 'user_list.html')
```

需要重新启动才会显示图片

app/static/image/xm.png
```python
{% load static %}
<!DOCTYPE html>
    <img src="{% static 'image/xm.png' %}" alt="" />
</html>
```

## 常用模板语法
app/views.py
```python
def user_list(request):
    name = 'zs'
    list = ['zs', 'ls', 'xr']
    dict = {"name":"xr"}
    flag = False
    return render(request, 'user_list.html', {
        "name": name,
        "list": list,
        "dict": dict,
        "flag": flag
    })
```
app/templates/user_list.html
```html
<div>
    <p>{{ list.0 }}</p>
    {% for it in list %}
        <p>{{ it }}</p>
    {% endfor %}
</div>

<div>
    {% for it in dict %}
        <p>{{ it }}</p>
    {% endfor %}
</div>

<div>
    {% if flag %}
        <p>True</p>
    {% else %}
        <p>False</p>
    {% endif %}
</div>
```

### 模板继承
app/templates/layouts.html
```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> {% block title %}  {% endblock %}</title>
</head>

<body>
    <div class="layout">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

使用继承
```python
{% extends 'layouts.html' %}

{% block title %}
    orm
{% endblock %}
{% block content %}
    <div>ormbb</div>
{% endblock %}
```

## 请求与响应
app/views.py
```python
from django.shortcuts import render, HttpResponse, redirect

def request(request):
    # request是一个对象，封装了用户发送来的所有请求相关的数据
    # method GET
    # print('method', request.method)
    # http://127.0.0.1:8000/request/?id=1&type=2 ==> GET <QueryDict: {'id': ['1'], 'type': ['2']}>
    # print('GET', request.GET)
    # print('POST', request.POST)

    # 响应
    # return HttpResponse('request')
    # 重定向 是由浏览器重定向
    # return redirect('http://www.baidu.com')

    if request.method == 'GET':
        return render(request, 'request.html')

    #  <QueryDict: {'csrfmiddlewaretoken': ['c5F6mUAlPwCx4sr4vrBUFmgahbFKntU5jzfsILC12ssT4wtSpwsniugHlHsVr7pH'], 'name': ['ad'], 'pwd': ['12']}>
    # print('===',request.POST)
    # return HttpResponse('登录成功')

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    if name == 'root' and pwd == '123':
        return HttpResponse('登录成功')
    return render(request, 'request.html', {'error_msg': "用户名密码错误"})

```
app/templates/request.html
```html
<form action="/request/" method="post">

    {% csrf_token %}

    <input type="text" name="name" placeholder="用户名">
    <input type="password" name="pwd" placeholder="密码">
    <input type="submit" value="提交">
</form>
<p>{{ error_msg }}</p>
```
动态传参
```python
 path('orm/<int:id>/edit/', views.orm),
```
http://127.0.0.1:8000/orm/2/edit/
```python
def orm(request,id):
    print(id) # 2
```



## 数据库操作

### 下载 mysqlclient

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple mysqlclient
```

### 创建数据库
```python
create database python
```


### Django 链接数据库

替换为 mysql 数据库
project/settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'python',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```
创建表和字段
app/models.py
```python
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password  = models.CharField(max_length=64)
    age = models.IntegerField()

```
执行命令
```python
python manage.py makemigrations
python manage.py migrate
```

### 数据库增删改查

```python
from app.models import UserInfo

def orm(request):
    # 增
    # UserInfo.objects.create(name='zs',password='123',age=18)
    # UserInfo.objects.create(name='xr',password='123',age=28)

    # 删
    # UserInfo.objects.filter(id=1).delete()
    # UserInfo.objects.all().delete()

    # 查
    # user_list = UserInfo.objects.all()
    # user_list = UserInfo.objects.filter(id=2)
    # dict = UserInfo.objects.filter(id=2).first()

    # 改
    UserInfo.objects.filter(id=2).update(age=66)
    return HttpResponse('orm')
```


时间格式转换
obj.create_time.strftime("%Y-%m-%d")