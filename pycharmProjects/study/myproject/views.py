from django.shortcuts import render,redirect
from myproject import models
# Create your views here.
def index(request):
    pass
    return render(request, 'myproject/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            print(username,password)
            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, 'myproject/login.html')
            if user.password == password:
                return redirect('/index/')
    return render(request, 'myproject/login.html')


def register(request):
    pass
    return render(request, 'myproject/register.html')


def logout(request):
    pass
    return redirect("/index/")