from django.db import models
from django.http import HttpResponse


# Create your models here.
class Carlist(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    #mnum=models.IntegerField()
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
       return self.name
