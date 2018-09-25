from django.shortcuts import render,redirect
# Create your views here.
def index(request):
    pass
    return render(request, 'myproject/index.html')


def login(request):
    pass
    return render(request, 'myproject/login.html')


def register(request):
    pass
    return render(request, 'myproject/register.html')


def logout(request):
    pass
    return redirect("/index/")