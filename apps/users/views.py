# _*_ encoding:utf-8 _*_
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        user_password = request.POST.get('password', '')
        users=authenticate(username=user_name, password=user_password)
        if users is not None:
            login(request, users)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': u'用户名或密码错误'})

    elif request.method =='GET':
        return render(request,'login.html',{})