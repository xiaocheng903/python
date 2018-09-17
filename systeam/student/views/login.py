from django.shortcuts import render,redirect,HttpResponse
from student import models
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

TOPIC_CHOICES = (
  ('leve1', '唱歌'),
  ('leve2', '跳舞'),
  ('leve3', '运动'),
)

class likeForm(forms.Form):
    like = forms.ChoiceField(label='爱好',choices=TOPIC_CHOICES)
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
                response = redirect('/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                # 失败 仍在login页面
                return redirect('login/')
    else:
        uf = UserForm()
    return render(req,'login.html',{'uf':uf})

def index(req):
    username = req.COOKIES.get('username','')
    print(username)
    return render(req,'index.html',{'username':username})

def data(req):
    username = req.COOKIES.get('username', '')
    print(username)
    if req.method == 'POST':
        lf = likeForm(req.POST)
        if lf.is_valid():
            like = lf.cleaned_data['like']
            food = lf.cleaned_data['food']
            insert = models.data.objects.create(username=username,like=like,eat=food)
            if insert:
                response = redirect('/check/')
                return response
    else:
        lf = likeForm()
    return render(req, 'data.html', {'uf':lf})

def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def check(req):
    dls_list = models.data.objects.all()
    return render(req,'check.html',{'dls_list':dls_list})



