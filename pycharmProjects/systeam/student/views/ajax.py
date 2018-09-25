from django.shortcuts import render,redirect,HttpResponse
from student import models
def ajax1(request):
    return render(request,'ajax1.html')

def ajax2(request):
    u=request.GET.get('username')
    p=request.GET.get('password')
    if u is not None:
        if p is not None:
            # #### 删除原先该名字的数据
            s=models.Login.objects.filter(username=u)
            if len(s)>0:
                models.Login.objects.filter(username=u).delete()
                print("删除数据成功")
            models.Login.objects.create(username=u, password=p)
            print("插入数据成功")
            return HttpResponse('欢迎你：' + u + '密码为：' + p)
        else:
            return HttpResponse('密码为空')
    else:
        return HttpResponse('姓名为空')




