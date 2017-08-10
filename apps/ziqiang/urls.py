# _*_ encoding:utf-8 _*_
from django.conf.urls import url

from .views import ZqIndexView, ZqAddView, AjaxListView


urlpatterns = [
    url(r'^index/', ZqIndexView.as_view(), name='index'),
    url(r'^add/', ZqAddView.as_view(), name='add'),
    url(r'^list/', AjaxListView.as_view(), name='list'),
]