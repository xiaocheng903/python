from django.contrib import admin
from django.urls import path
from student.views import classes,students,teachers,ajax,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes.html',classes.getClasses),
    path('add_classes.html', classes.addClasses),
    path('del_classes.html', classes.delClasses),
    path('get_teachers.html', teachers.getTeachers),
    path('get_student.html',students.getStudent),
    path('set_teachers.html', classes.set_teachers),
    path('ajax1.html', ajax.ajax1),
    path('ajax2.html', ajax.ajax2),

    path('regist', login.regist),
    path('login', login.login),
    path('like', login.like),
    path('error', login.error),
]
