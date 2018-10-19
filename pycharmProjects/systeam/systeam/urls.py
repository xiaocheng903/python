from django.contrib import admin
from django.urls import path
from student.views import classes,students,teachers,ajax,login,csv,TemplateView

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

    path('account/regist/', login.regist),
    path('account/login/', login.login),
    # path('account/index/', login.index),
    path('account/data/', login.data),
    path('account/logout/', login.logout),
    path('account/check/', login.check),
    path('account/uploadFile/', login.uploadFile),
    path('account/some_view/', csv.some_view),

    path('', TemplateView.home.as_view()),
    path('account/index/', TemplateView.index.as_view()),
    # path('student/testapi', TemplateView.testapi),
]
