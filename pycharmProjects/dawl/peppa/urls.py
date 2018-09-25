"""dawl URL Configuration

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
from peppa import views



urlpatterns = [
    path('', views.home.as_view()),
    path('apply', views.apply.as_view()),
    path('applysave', views.applysave.as_view()),
    path('status', views.status.as_view()),
    path('sqlstatus', views.sqlstatus.as_view()),
    path('projectDetail', views.projectDetail.as_view()),
    path('applysql', views.applysql.as_view()),
    path('applysqlsave', views.applysqlsave.as_view()),
    path('sqlDetail', views.sqlDetail.as_view()),
    path('release_status', views.release_status.as_view()),
    path('version', views.version.as_view()),
    path('query_verinfo', views.query_verinfo),
    path('release_page', views.release_page.as_view()),
    path('project_release', views.project_release.as_view()),
    path('test', views.test),
    path('releStatu', views.releStatu),
    path('select_env', views.select_env),

]
