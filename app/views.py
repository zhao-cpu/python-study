from django.shortcuts import render, HttpResponse, redirect
from app.models import UserInfo
# Create your views here.


def index(request):
    return HttpResponse('index 函数')


def user_list(request):
    name = 'zs'
    list = ['zs', 'ls', 'xr']
    dict = {"name": "xr"}
    flag = False
    return render(request, 'user_list.html', {
        "name": name,
        "list": list,
        "dict": dict,
        "flag": flag
    })


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
    # get_字段名_display() dict.get_gender_display()
    # dict.deaprt_id 获取连表 id    dict.连表字段.字段名 dict.deaprt.title 获取连表id对应的值

    # 改
    # UserInfo.objects.filter(id=2).update(age=66)
    

    return render(request,'orm.html')