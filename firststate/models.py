from django.db import models

# Create your models here.
class Course_1(models.Model):
    text= models.TextField()
    description=models.TextField()
    url= models.URLField()