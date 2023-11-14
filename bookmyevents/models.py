from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phoneNumber=models.CharField(default='',max_length=10)
    email=models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50)
class Events(models.Model):
    eventName=models.CharField(max_length=50)
    eventgenre=models.CharField(max_length=50)
    eventPrice=models.IntegerField()
    eventImage=models.ImageField(upload_to='images/')
    eventDate=models.DateField()
    numberOfTickets=models.IntegerField()
class Booking(models.Model):
    bookedBy=models.CharField(max_length=50)
    bookedEvent=models.CharField(max_length=50)
    bookedDate=models.DateField()
    bookedtickets=models.IntegerField()
    bookedprice=models.IntegerField()
class Payment(models.Model):
    paidBy=models.CharField(max_length=50)
    paidEvent=models.CharField(max_length=50)
    paidDate=models.DateField()
    paidtickets=models.IntegerField()
    paidprice=models.IntegerField()
    paidStatus=models.CharField(max_length=50)