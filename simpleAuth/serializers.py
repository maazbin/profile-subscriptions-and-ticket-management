# from dataclasses import fields
# from pyexpat import model
from rest_framework import serializers
from simpleAuth.models import  CustomUser


# from django.contrib.auth import get_user_model

# User = get_user_model()



class UserSerializers(serializers.ModelSerializer):

    class Meta :
        model = CustomUser
        fields = ['id','first_name','last_name']

# this serializer handles data for signup view
class SignupSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','email']



# this serializer handles data for login view
class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name']    