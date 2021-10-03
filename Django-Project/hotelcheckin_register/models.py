from django.db import models

# Create your models here.

class Hotel(models.Model):
    genderTypes = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'None')
    )

    roomTypes = (
        ('D','DELLUXE ROOMS ( 200$ )'),
        ('J','JUNIOR SUITE ( 250$ )'),
        ('G','GRAND SUITE ( 300$ )')
    )

    fullname = models.CharField(max_length=100)
    email = models.EmailField(db_column='Email', max_length=60)
    contact = models.CharField(db_column='Contact_No', max_length=20)
    gender = models.CharField(choices=genderTypes, max_length=10, default="N")
    roomtype = models.CharField(choices=roomTypes, max_length=100, default="D")
    checkstatus = models.BooleanField(db_column='Checkin Status')
    age = models.IntegerField(db_column='Age')
    date_of_join = models.DateField(db_column='Date_Of_Join') 
    income = models.FloatField(db_column='income')
    address = models.TextField(db_column='Address')
    hotelImg = models.ImageField(db_column='Image',upload_to='',null=True)

    
