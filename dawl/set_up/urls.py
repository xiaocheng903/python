from django.urls import path
from set_up import views

urlpatterns = [
    path('', views.setup),
    path('add_user',views.add_user_group),
    path('add_project',views.add_project),
    path('add_theme',views.add_theme),
    path('logout',views.logout),

]
