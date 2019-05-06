from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    major = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=14)
