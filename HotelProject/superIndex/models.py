from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete='models.CASCADE')
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=264)
    address = models.CharField(max_length=264)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    gender = models.CharField(max_length = 9,choices=SEX_CHOICES)
    govt_proof = models.CharField(max_length = 264)
    contact_num = models.BigIntegerField()


    def __str__(self):
        return str(self.cust_name)

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length = 264)
    room_num = models.CharField(max_length = 264)
    floor = models.CharField(max_length = 264)
    avail = models.CharField(max_length = 264)
    price = models.CharField(max_length = 264)

    def __str__(self):
        return str(self.room_num)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.CharField(max_length = 264)


    def __str__(self):
        return str(self.room_id)
