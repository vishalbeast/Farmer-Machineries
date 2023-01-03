from django.db import models
import os


# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=30,  null=True)
    MobileNumber = models.IntegerField()
    Address = models.CharField(max_length=80,  null=True)
    pincode = models.CharField(max_length=6,  null=True)
    image = models.ImageField(upload_to=os.path.join(os.getcwd() , 'static' , 'images'))
    rentalamount = models.IntegerField(default=0)
    tractormodel = models.CharField(max_length=30,  null=True)


class User(models.Model):
    name = models.CharField(max_length=30,  null=True)
    numofhours = models.IntegerField()
    datetime = models.DateTimeField(default=None)
    address = models.CharField(max_length=100,  null=True)
    pincode = models.CharField(max_length=6,  null=True)


class Hire(models.Model):
    name = models.CharField(max_length=30 , null=True)
    numofdays = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=None)
    address = models.CharField(max_length=100 , null=True)
    pincode = models.CharField(max_length=6 ,  null=True)
