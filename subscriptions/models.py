from django.db import models
from django.db.models import CASCADE,DO_NOTHING 
import time
import uuid

# from datetime import datetime,timedelta

from datetime import timedelta, date

# import models

from simpleAuth.models import CustomUser
# from cars.models import Car


class SubscriptionType(models.Model):

    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return f'{self.name}'

class Subscription(models.Model):

    serial_no = models.CharField(default = uuid.uuid4, unique=True,max_length=100)    
    date_of_purchase = models.DateField(default = date.today())
    
    # start_time = models.TimeField(default=time.localtime())
    date_of_expiry = models.DateField(
        default = date.today() + timedelta(days=30)
    )
    # end_time = models.TimeField(default=time.localtime())
    user = models.ForeignKey(CustomUser,on_delete=CASCADE)
    subscription_type = models.ForeignKey(SubscriptionType,on_delete=CASCADE)
    is_approved = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     self.serial_no = self.serial_no.upper()
    #     return super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        if self.is_approved:
            return f'{self.date_of_purchase} to {self.date_of_expiry} , {self.subscription_type} , Approved'
        return f'{self.date_of_purchase} to {self.date_of_expiry} , {self.subscription_type}, Not Approved'



    