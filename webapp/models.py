from django.db import models

# Create your models here.
class regdb(models.Model):
    rname = models.CharField(max_length=100,null=True,blank=True)
    remail = models.CharField(max_length=100,null=True,blank=True)
    rmobile = models.IntegerField(max_length=100,null=True,blank=True)
    rpas = models.CharField(max_length=100,null=True,blank=True)
    rimage = models.ImageField(upload_to='user',null=True,blank=True)

class cartdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)

    description = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)
class billdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
