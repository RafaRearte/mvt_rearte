from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth_date = models.DateField()
    occupation = models.CharField(max_length=40)
    relation = models.CharField(max_length=40)