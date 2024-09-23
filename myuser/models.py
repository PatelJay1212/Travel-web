from django.db import models
from django.contrib.auth.models import User
from myadmin.models import Packages

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=250,null=True,blank=True)
    beneficiary_name = models.CharField(max_length=250,null=True,blank=True)
    ifsc_code = models.CharField(max_length=250,null=True,blank=True)
    card_number = models.IntegerField(null=True,blank=True)
    card_expiry = models.IntegerField(null=True,blank=True)
    cvv = models.IntegerField(null=True,blank=True)


class Book(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    email= models.EmailField()
    datetime = models.DateTimeField()
    person = models.IntegerField()
    child = models.IntegerField()
    message = models.CharField(max_length=250)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"booking by {self.user.username}"



    


    
