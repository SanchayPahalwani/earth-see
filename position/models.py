from django.conf import settings
from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.name

class Position(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    coords = models.CharField(max_length=200, unique=True)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.coords