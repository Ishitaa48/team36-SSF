from django.db import models

# Create your models here.
class NineTen(models.Model):
    Question=models.TextField(max_length=500)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)
    ans=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    Taxonomy=models.CharField(max_length=100)

class Inter(models.Model):
    Questions=models.TextField(max_length=500)
    opt1=models.CharField(max_length=100)
    opt2=models.CharField(max_length=100)
    opt3=models.CharField(max_length=100)
    opt4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    Taxonomy=models.CharField(max_length=100)
