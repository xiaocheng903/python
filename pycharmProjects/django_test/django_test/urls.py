"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miaTest import views
from rest_framework.urlpatterns import format_suffix_patterns

# 调用views内对应的方法
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('create/', views.create),
    path('show/', views.show),
    path('query/', views.query),
    path('getlist/', views.getlist),
]
urlpatterns = format_suffix_patterns(urlpatterns)