# _*_ encoding:utf-8 _*_
from django.conf.urls import url

from .views import CourseListView


urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='list'),
]