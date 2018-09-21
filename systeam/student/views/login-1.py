from django.shortcuts import render,redirect,HttpResponse
from student import models
from django.contrib.auth import authenticate, login
from django import forms

import json

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

def my_view(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(req, user)
                #比较成功，跳转至登录成功界面
                response = redirect('/account/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponse('用户名或密码失败')

        return render(req,'login.html',locals())
    else:
        uf = UserForm()
    return render(req,'login.html',locals())



