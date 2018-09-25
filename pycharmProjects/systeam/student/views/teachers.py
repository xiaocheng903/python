from django.shortcuts import render,redirect
from student import models
def getTeachers(request):
    tea_list = models.Classes.objects.all()
    return render(request,'get_teachers.html',{'tea_list':tea_list})