from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from user.models import UserModel, UserSession
from utils.functions import get_session

def home(request):
    if request.method == 'GET':
        return render(request,'index.html')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        data={}
        if not all([username, password]):
            data['msg']='The information is incomplete'
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            if check_password(password,user.password):
                session=get_session()
                res= HttpResponseRedirect(reverse('app:index'))
                out_time=datetime.now() + timedelta(days=1)
                res.set_cookie('session',session,expires=out_time)
                UserSession.objects.create(user=user,session=session,out_time=out_time)
                return res
            else:
                data['msg']='Unkown username or password Error'
        else:
            data['msg']='Unkown username or password Error'
        return render(request, 'login.html', data)


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email=request.POST.get('email')
        if not all ([username, pwd, cpwd, email]):
            return render(request,'login.html')
        password = make_password(pwd)
        UserModel.objects.create(username=username, password=password,email=email)
        return HttpResponseRedirect(reverse('user:login'))


def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('user:home'))
        response.delete_cookie('session')
        return response