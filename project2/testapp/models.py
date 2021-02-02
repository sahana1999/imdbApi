from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    gender=models.CharField(max_length=15)