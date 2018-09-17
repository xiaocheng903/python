from django.db import models

# Create your models here.
class Classes(models.Model):
    title = models.CharField(max_length=32)
    a = models.ManyToManyField('Teachers')

class Teachers(models.Model):
    name = models.CharField(max_length=32)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE)

class Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __unicode__(self):
        return self.username

class data(models.Model):
    username = models.CharField(max_length=32)
    like = models.CharField(max_length=32)
    eat = models.CharField(max_length=32)