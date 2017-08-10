# _*_ encoding:utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse

from random import randint


class ZqIndexView(View):
    def get(self, request):
        return render(request, template_name='indexzq.html')


class ZqAddView(View):
    def get(self, request):
        a = request.GET.get('a', '')
        b = request.GET.get('b', '')
        try:
            a = int(a)
            b = int(b)
            return HttpResponse(str(a+b))
        except:
            return HttpResponse(u'请重新输入')


# def index(request):
#     return render(request, 'indexzq.html')
#
#
# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     a = int(a)
#     b = int(b)
#     return HttpResponse(str(a + b))

class AjaxListView(View):
    def get(self, request):
        data = randint(1, 5)
        a = range(data)
        return JsonResponse(a, safe=False)

