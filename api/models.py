from django.db import models
import datetime
import os

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" %(timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField(upload_to=filepath, null = True, blank= True )
    date_Add = models.DateField()

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField(upload_to=filepath, null = True, blank= True )
    date_Add = models.DateField()

