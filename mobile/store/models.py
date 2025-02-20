from django.db import models

from db_connection import db

#Create your models here.


store_collection = db['store']

from django import models

class Mobile(models.Model):
  name= models.CharField(max_length=200) 
  brand= models.CharField(max_length=100)
  price= models.FloatField()
  specifications= models.TextField()
  image= models. ImageField(upload_to='mobiles/')

  def _str_(self):
     return self.name

class Cart(models.Model):
    user= models.CharField(max_length=100)
    mobile= models. Foreignkey (Mobile, on_delete=models.CASCADE)
    quantity = models. IntegerField(default=1)