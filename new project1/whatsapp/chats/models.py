from django.db import models

# Create your models here.

class record(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=255)
