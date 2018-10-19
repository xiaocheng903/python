from django.shortcuts import render,redirect,HttpResponse
from student import models
from django import forms
from django.contrib.auth.decorators import login_required

from .Form import uploadfileForm
from systeam import settings
# from .handle_uploaded_file import handle_uploaded_file

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
            userId = models.Login.objects.filter(username__exact= username)
            user = models.Login.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转至登录成功界面
                print("登录成功")
                response = redirect('/account/index/')
                #将username写入浏览器cookie,失效时间为3600
                # response.set_cookie('username',username,3600)
                # req.session['is_login'] = '1'
                # req.session['username']=username
                return response
            elif userId:
                message = "密码不正确"
                print(message)
            else:
                # 失败 仍在login页面
                message = "用户不存在"
                print(message)
                return redirect('/account/regist')
        return render(req,'login.html',locals())
    else:
        uf = UserForm()
    return render(req,'login.html',locals())

# @login_required
def index(req):
    username = req.COOKIES.get('username','')
    print(username)
    userobj = models.Login.objects.filter(username=username)
    if userobj:
        message = '登录成功'
        print(message)
        return render(req,'index.html',locals())
    else:
        return redirect('/account/login')

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
                response = redirect('/account/check/')
                return response
    else:
        lf = likeForm()
    return render(req, 'data.html', {'uf':lf})

def logout(req):
    req.session.flush()
    return redirect('/')

def check(req):
    dls_list = models.data.objects.all()
    return render(req,'check.html',{'dls_list':dls_list})

def uploadFile(req):
    if req.method == 'POST':
        form = uploadfileForm(req.POST,req.FILES)
        if form.is_valid():
            handle_uploaded_file(req.FILES['file'])
            return HttpResponse('上传成功')
    else:
        form = uploadfileForm()
    return render(req, 'upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('../name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
