from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    age = models.IntegerField()
