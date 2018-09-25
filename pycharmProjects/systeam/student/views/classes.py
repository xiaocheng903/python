from django.shortcuts import render,redirect
from student import models
def getClasses(request):
    cls_list = models.Classes.objects.all()
    return render(request, 'classes.html', {'cls_list':cls_list})

def addClasses(request):
    if request.method == 'GET':
        return render(request,'add_Classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        # 添加新的班级，插入数据库
        models.Classes.objects.create(title=title)
        return redirect('/classes.html')

def delClasses(request):
    nid = request.GET.get('nid', '')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')

# 为班级设置老师
def set_teachers(request):
    if request.method == 'GET':
        nid = request.GET.get('nid','')
        cls_obj = models.Classes.objects.get(id = nid)
        cls_teacher_list = cls_obj.a.all()
        all_teacher_list = models.Teachers.objects.all()
        return render(request, 'set_teachers.html', {
            'cls_teacher_list': cls_teacher_list,
            'all_teacher_list': all_teacher_list,
            'nid': nid,
        })
    elif request.method == 'POST':
        nid = request.POST.get('nid', '')
        ids_str = request.POST.getlist('teacher_id', '')
        ids_int = []
        for i in ids_str:
            i = int(i)
            ids_int.append(i)
        obj = models.Classes.objects.get(id=nid)
        obj.a.set(ids_int)
        return redirect('/classes.html')

