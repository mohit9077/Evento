from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django_cryptography.fields import encrypt

# Create your models here.

class login_admin(models.Model):
    club = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class login_user(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)


class UserReg(models.Model):
   
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    email=models.EmailField()
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    
    def get_fullname(self):
        """
        Return the fullname
        :return: fullname
        """
        fullname = '{} {}'.format(self.f_name, self.l_name)
        return fullname



class AdminReg(models.Model):
    
    club = models.CharField(max_length=20)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)


    def __str__(self):
        return self.club








class eventregmodel(models.Model):
    fname = models.CharField(default ="NULL",max_length=100)
    lname = models.CharField(default ="NULL",max_length=100)
    usn = models.CharField(default ="NULL",max_length=100)
    email = models.EmailField(default = "NULL")
    branch = models.CharField(default ="NULL",max_length=100)
    club = models.CharField(default ="NULL",max_length=100)
    event_title = models.CharField(default ="NULL",max_length=100)




