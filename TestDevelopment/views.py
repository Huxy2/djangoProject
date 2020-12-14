from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        data = [
            {
                'project_name': '天宫二号',
                'leader': '科研人',
                'app_name': '探月',
            },
            {
                'project_name': '测试开发平台',
                'leader': '大头',
                'app_name': '代码应用',
            },
        ]
        # return render(request, 'demo1.html', locals())
        return JsonResponse(data, safe=False)

    def post(self, request):
        return HttpResponse('post请求')

    def put(self, request):
        return HttpResponse('put请求')

    def delete(self, request):
        return HttpResponse('delete请求')
