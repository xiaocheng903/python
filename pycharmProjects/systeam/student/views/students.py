from django.shortcuts import render,redirect
from student import models
def getStudent(request):
    stu_list = models.Classes.objects.all()
    return render(request,'get_student.html',{'stu_list':stu_list})





