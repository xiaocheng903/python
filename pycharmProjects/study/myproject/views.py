from django.shortcuts import render,redirect,HttpResponse
from myproject import models
import pymysql
from django import forms
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    pass
    return render(request, 'myproject/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username and password:
            username = username.strip()
            print(username,password)
            user = models.User.objects.filter(name__exact = username,password__exact = password)
            if user:
                return redirect('/index/')
            else:
                message = '用户名/密码不正确'
                return render(request, 'myproject/login.html',{'message':message})
        else:
            message = '账号或密码不能为空'
            return render(request, 'myproject/login.html', {'message': message})
    return render(request, 'myproject/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        email = request.POST.get('email',None)
        sex = request.POST.get('sex',None)
        time = request.POST.get('time',None)
        print(username,password,email,sex,time)
        models.User.objects.create(name=username,password=password,email=email,sex=sex,c_time=time)
        return HttpResponse('注册成功')
    return render(request, 'myproject/register.html')


def logout(request):
    request.session.flush()
    return redirect("/login/")

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    database="practice"
)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

class UserForm(forms.Form):
    sno = forms.CharField(label='学号',max_length=100,required=False)
    sname = forms.CharField(label='姓名',max_length=100,required=False)
    Aclass = forms.CharField(label='班级',max_length=100,required=False)

@csrf_exempt
def query(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            sno = uf.cleaned_data['sno']
            sname = uf.cleaned_data['sname']
            Aclass = uf.cleaned_data['Aclass']
            print(sno,sname,Aclass)
            sql = "select sno,sname,class as Aclass from students where sno like '%%%%%s%%%%' and " \
                  "sname like '%%%%%s%%%%' and class like '%%%%%s%%%%'"%(sno,sname,Aclass)
            print(sql)
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                results = json.dumps(results)
                print(results)
                return render(request, 'myproject/query.html', locals())
            except:
                print("Error: unable to fetch data")
    uf = UserForm()
    return render(request, 'myproject/query.html',locals())






