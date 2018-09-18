from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.http import require_http_methods
from peppa import models as peppa_models
from django.contrib.auth.models import User
# Create your views here.


def setup(request):
    if not request.user.username == 'admin':
        return HttpResponse('无权限访问')
    return render(request, 'test/setup.html')


#添加人员
@require_http_methods(['GET', 'POST'])
def add_user_group(request):
    if not request.user.username == 'admin':
        return HttpResponse('无权限访问')
    if request.method == 'GET':
        return render(request, 'test/add_user.html')
    else:
        username = request.POST.get('username')
        name = request.POST.get('name')
        role = request.POST.get('role')
        group = request.POST.get('group')
        level = request.POST.get('leader')
        password = request.POST.get('password')
        mail = request.POST.get('mail')
        user = User.objects.create_superuser(username, mail, password)
        print('注册人员信息%s成功' % name)
        obj = peppa_models.User_Grpup(name=name,
                                      username=username,
                                      role=role,
                                      group=group,
                                      level=level,
                                      mail=mail)
        obj.save()
        print('添加人员信息%s成功' % name)

        return render(request, 'test/add_user.html')


#添加项目
@require_http_methods(['GET', 'POST'])
def add_project(request):
    if not request.user.username == 'admin':
        return HttpResponse('无权限访问')
    if request.method == 'GET':
        return render(request, 'test/add_project.html')
    else:
        project = request.POST.get('project')
        name = request.POST.get('name')
        gitaddress = request.POST.get('gitaddress')
        group = request.POST.get('group')
        print('project = ', project, 'name = ', name, 'gitaddress = ', gitaddress, 'group = ', group)

        return render(request, 'test/add_project.html')


#更改首页联系人
def add_theme(request):
    return HttpResponse('add_theme')

def logout(request):
    request.session.flush()
    return  redirect('/peppa')