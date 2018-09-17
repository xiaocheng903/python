from django.shortcuts import render,redirect,HttpResponse
from student import models
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

TOPIC_CHOICES = (
  ('leve1', '差评'),
  ('leve2', '中评'),
  ('leve3', '好评'),
)

class likeForm(forms.Form):
    like = forms.ChoiceField(label='选择喜欢的',choices=TOPIC_CHOICES)
    food = forms.CharField(label="爱吃的",max_length=100)

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            models.Login.objects.create(username= username,password=password)
            return HttpResponse("success")
    else:
        uf=UserForm()
    return render(req,'regist.html',{'uf':uf})

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = models.Login.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转至登录成功界面
                response = redirect('/like')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return redirect('login/')
    else:
        uf = UserForm()
    return render(req,'login.html',{'uf':uf})

def like(request):
    if request.method == 'GET':
        return render(request,'like.html')

    elif request.method == 'POST':
        like = request.POST.get('like', '')
        eat = request.POST.get('eat','')
        u = request.GET.get('username')
        print(u)
        print(like)
        print(eat)
        models.data.objects.create(username=u,like=like,eat=eat)
        return redirect('/like.html')

def error(request):
    if request.method == 'GET':
        return render(request,'error.html')