# _*_ encoding:utf-8 _*_
from django.conf.urls import url
from django.views.generic.base import TemplateView
# from .views import

urlpatterns = [
    url(r'info/$', TemplateView.as_view(template_name='usercenter-info.html'), name='info'),

]
