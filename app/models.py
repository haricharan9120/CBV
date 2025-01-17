from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=50)
    scprincipal=models.CharField(max_length=50)
    sclocation=models.CharField(max_length=50)
    def __str__(self):
        return self.scname
    def get_absolute_url(self):
        return reverse('schooldetail',kwargs={'pk':self.pk})
    
class Student(models.Model):
    stname=models.CharField(max_length=50)
    stage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    def __str__(self):
        return self.stname
