from django.db import models

# Create your models here.

class general(models.Model):
    title = models.CharField(max_length=50)
    club = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 1000)
    date = models.DateTimeField()
    venue = models.CharField(max_length = 50)
    title_type = models.CharField(max_length=50)




    
