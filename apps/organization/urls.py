# _*_ encoding:utf-8 _*_

from django.conf.urls import url

from .views import OrgView, UserAskView

urlpatterns = [
    url(r'list/$', OrgView.as_view(), name='list'),
    url(r'add_ask/$', UserAskView.as_view(), name='add_ask'),
]
