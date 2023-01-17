# from statistics import mode
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager #user manager class

from django.utils.timezone import now

'''
This is custom user class where we can add fields which are not by default provided 
in django user model. This user model can be accessed through authApp
'''
class CustomUser(AbstractUser):
    # username = None
    id = models.CharField(default = uuid.uuid4, primary_key=True,max_length=100)
   
    # is_staff = models.BooleanField(default=False)
   
    creation_date = models.DateTimeField(default=now, editable=True)
    username = None
    email = models.EmailField( unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email