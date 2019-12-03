from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 显示登陆页面
def myhome_login(request):
    return render(request,'myhome/login/login.html')


# 执行登陆
def myhome_dologin(request):
    return HttpResponse('myhome_dologin')


# 显示注册页面
def myhome_register(request):
    return render(request,'myhome/login/register.html')


# 执行注册
def myhome_doregister(request):
    return HttpResponse('myhome_doregister')
