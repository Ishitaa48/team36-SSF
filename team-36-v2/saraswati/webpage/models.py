from django.db import models

# Create your models here.
class teacher_db(models.Model):
    teacher_nm = models.CharField(max_length=30)
    email = models.CharField(max_length=30) 
    password = models.CharField(max_length=30)
    
class student_db(models.Model):
    student_nm = models.CharField(max_length=30)
    email = models.CharField(max_length=30) 
    password = models.CharField(max_length=30)
    