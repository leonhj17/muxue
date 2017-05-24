# _*_ encoding:utf-8 _*_
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import LoginForm, RegisterForm
# Create your views here.

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm(request.POST)
        return render(request, 'register.html', {'registerform': register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = request.POST.get('email')
            user_name = request.POST.get('email')
            user_password = make_password(request.POST.get('password'))
            user = UserProfile()
            user.username= user_name
            user.email = user_email
            user.password = user_password
            user.save()

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            user_password = request.POST.get('password', '')
            users = authenticate(username=user_name, password=user_password)
            if users is not None:
                login(request, users)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': u'用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})



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