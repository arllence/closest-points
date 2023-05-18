from django.db import models

# Create your models here.
from django.db import models

class Point(models.Model):
    coordinates = models.CharField(max_length=255)
    closest_points = models.CharField(max_length=255)
