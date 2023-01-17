# from django.db import models
from django.db import models
from django.db.models import CASCADE,DO_NOTHING 
# import time
import uuid

from datetime import timedelta, date# datetime.today() - timedelta(days=self.days)

# import models

from simpleAuth.models import CustomUser



class IssueType(models.Model):
    
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f'{self.name}'



class Ticket(models.Model):
    ticket_id = models.CharField(default = uuid.uuid4, primary_key=True,max_length=100)
    user_id = models.ForeignKey(CustomUser,on_delete=CASCADE)
    ticket_date = models.DateField(default = date.today())
    ticket_description = models.TextField(max_length=255)
    issue_type = models.ForeignKey(IssueType,on_delete=CASCADE)

    ticket_status = models.CharField(max_length=100,null=True,default='Open')

    def __str__(self) -> str:
        return f'{self.user_id} , {self.ticket_status}'