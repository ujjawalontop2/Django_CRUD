from django.db import models

# Create your models here.

class Tutorials(models.Model):
    objects = models.manager
    title = models.CharField(max_length=50,blank=False)
    description = models.CharField(max_length=254,blank=False)
    published = models.BooleanField(default=False)
