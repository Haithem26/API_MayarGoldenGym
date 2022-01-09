from django.db import models
import datetime
import os
#from django.contrib.auth.models import AbstractUser

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
'''
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS = []
'''
    

