# _*_ encoding:utf-8 _*_
from django.conf.urls import url

from .views import CourseListView, CourseDetailView


urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='list'),
    url(r'^detail/(?P<course_id>\d+)', CourseDetailView.as_view(), name='detail'),
]