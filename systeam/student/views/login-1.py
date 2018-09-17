from django.shortcuts import render,redirect,HttpResponse
from student import models
import json
def login(request):
    return render(request,'login.html')

def login_result(request):
    u=request.GET.get('username')
    p=request.GET.get('password')
    print(u)
    print(p)
    if u is not None:
        if p is not None:
            s=models.Login.objects.filter(username=u,password=p)
            if len(s)>0:
                print("密码正确")
                status = 1
                result = "success!"
                return HttpResponse(json.dumps({
                    "status": status,
                    "result": result,
                    "user": u
                }))
            else:
                print("密码错误")
                status = 0
                result = "error!"
                return HttpResponse(json.dumps({
                    "status": status,
                    "result": result
                }))

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

