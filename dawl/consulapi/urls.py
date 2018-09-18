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
from consulapi import views



urlpatterns = [
    path('', views.consul_update.as_view()),
    path('get_consul', views.get_consul.as_view()),
    path('update_consul', views.update_consul.as_view()),
    path('rollback_consul', views.rollback_consul.as_view()),
    path('get_consul_ajax', views.get_consul_ajax),
    path('update_consul_ajax', views.update_consul_ajax),
    path('rollback_consul_ajax', views.rollback_consul_ajax),
    path('roll_update', views.roll_update),
    path('consul_error', views.consul_error.as_view()),

]
