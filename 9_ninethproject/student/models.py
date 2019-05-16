from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=10) # 이름
    department = models.CharField(max_length=20) # 학과
    admission_year = models.IntegerField() # 입학년도
    student_number = models.IntegerField() # 학번
    level = models.IntegerField() # 학년
    grade_avg = models.FloatField() # 평균 학점
