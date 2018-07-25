from django.db import models

# Create your models here.
class Tango(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Name(models.Model): # creates tango_with_jango_name table
    name = models.CharField(max_length=50)