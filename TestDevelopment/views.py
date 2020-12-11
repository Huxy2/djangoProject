from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def index(request):
    """
    index视图函数
    :param request:
    :return:
    """
    return HttpResponse('hello django')


def index1(request):
    """
    index视图函数
    :param request:
    :return:
    """
    return HttpResponse('测试开发')


def my_name(request):
    name = '花生'
    return HttpResponse(f'我的名字是{name}')


def test_method(request):
    if request.method == 'GET':
        return HttpResponse('GET请求')
    elif request.method == 'POST':
        return HttpResponse('POST请求')
    else:
        return HttpResponse('NULL')


class MyView(View):

    def get(self, request):
        # return HttpResponse('get请求')
        return render(request, 'demo.html')

    def post(self, request):
        return HttpResponse('post请求')

    def put(self, request):
        return HttpResponse('put请求')

    def delete(self, request):
        return HttpResponse('delete请求')
