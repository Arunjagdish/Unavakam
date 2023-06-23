from django.db import models


# Create your models here.
class feedbacktable(models.Model):
    name = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=40,default="")
    age = models.IntegerField(default="")
    dining = models.CharField(max_length=30,default="")
    recommend = models.CharField(max_length=30, default="")
    favorite = models.CharField(max_length=30,default="")
    improve = models.CharField( max_length=30,default="")
    comment = models.CharField(max_length=30, default="")

class bookingtable(models.Model):
    firstname = models.CharField(max_length=30,default="")
    lastname = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=40,default="")
    phone = models.CharField(max_length=30,default="")
    date = models.DateField(max_length=30,default="")
    time = models.TimeField(max_length=30,default="")
    counts = models.IntegerField(default="")
    additional = models.CharField(max_length=50,default="")



    

