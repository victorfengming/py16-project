from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 首页
def myhome_index(request):
    return render(request, 'myhome/index/index.html')


# 列表
def myhome_list(request):
    return render(request, 'myhome/index/list.html')


# 详情
def myhome_info(request):
    return render(request, 'myhome/index/info.html')
