from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from miaTest import models
from miaTest import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 将请求定位到index.html文件中
def index(request):
    return render(request,'index.html')

# 插入数据
def create(request):
    models.Person.objects.create(name='xiaoli', age=18)
    print("插入成功")
    # s = models.Person.objects.get(name='xiaoli')
    # print(s)
    return HttpResponse("OK")
# 查询数据 后台数据库数据传送到前端
def show(request):
    s = models.Person.objects.all()
    return render(request,'show.html',{'s': s})

# 查询数据2
def query(request, format=None):
    MiatestPerson = models.MiatestPerson.objects.all()
    serializer = serializers.MeiziSerializer(MiatestPerson, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getlist(request, format=None):
    if request.method == 'GET':
        MiatestPerson = models.MiatestPerson.objects.all()
        serializer = serializers.MeiziSerializer(MiatestPerson, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.MeiziSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
