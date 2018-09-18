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
from django.urls import path,include
from peppa import views
from django.conf import settings
from django.conf.urls.static import static
from set_up  import views as set_up_views

from django.http import HttpResponse
from django.contrib.auth.views import login, logout_then_login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('peppa/', include("peppa.urls")),
    path('', views.home.as_view()),
    path('setup/',include("set_up.urls")),
    path('consulapi/', include("consulapi.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


