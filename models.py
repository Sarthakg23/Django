from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator, MaxLengthValidator, \
    MinLengthValidator

import datetime



# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100,unique=True, blank=True)
    age = models.IntegerField(blank=True,null=True,validators=[MaxValueValidator(150),MinValueValidator(0)])
    email = models.CharField(max_length=256, validators=[EmailValidator],null=True,unique=True)
    password = models.CharField(max_length=10,blank=False,null=False,default="123456")
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)
    mob = models.CharField(max_length=12,blank=True, null=True, validators=[MaxLengthValidator(12), MinLengthValidator(10)])
    address = models.CharField(max_length=100, blank=True, null=False,)
    ACC_TYPE = (
        ('C', 'Current_Account'),
        ('S', 'Saving_Account'),
        ('F', 'Fixed_Deposit'),
        ('R', 'Recurring_Deposit')
    )
    account_type = models.CharField(max_length=20, choices=ACC_TYPE)
    balance = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(0)])





    def __str__(self):
        return self.name


class Debit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.IntegerField(blank=False,null=True)
    description =  models.CharField(max_length=100,blank=False,null=False,default="Balance")
    date = models.DateField(("Date"), default=datetime.date.today)

class Credit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.IntegerField(blank=False,null=True,validators=[MaxValueValidator(50000),MinValueValidator(500)])
    description = models.CharField(max_length=100, blank=False, null=False, default="Balance")
    date = models.DateField(("Date"), default=datetime.date.today)

class Transfer(models.Model):
    user = models.ForeignKey(User, null=True, related_name='user',on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, related_name='receiver',on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False,null=True,validators=[MinValueValidator(500)])
    description = models.CharField(max_length=100, blank=False, null=False, default="Transfer")
    date = models.DateField(("Date"), default=datetime.date.today)


