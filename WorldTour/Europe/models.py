from django.db import models

# Create your models here.
class Trip(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    price = models.IntegerField()
    night = models.IntegerField() 
    
    night2 = models.IntegerField() 
    night3 = models.IntegerField() 
    night4 = models.IntegerField() 