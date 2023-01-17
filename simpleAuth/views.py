
from .models import CustomUser
# from django.contrib.auth import authenticate
# from django.shortcuts import redirect
# from django.urls import reverse

# Django rest framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# from django.contrib.auth.hashers import make_password #encrypt password

#serializers 
from simpleAuth.serializers import (
    LoginSerializers,
    SignupSerializers,
)

# compare hashed passwored with requested user password
from django.contrib.auth.hashers import check_password
# create hashed password
from django.contrib.auth.hashers import make_password



'''
you have to define User with the Custom User model and you can do this 
with get_user_model at the top of the file where you use User
'''
# from django.contrib.auth import get_user_model

#

@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']
    # if check_password('the default password', u.password)

    error = {'error':'invalid credentials', 'msg':'Failiour'}

    try:
        user = CustomUser.objects.get(email=email)

        #if password doesnt match
        if not check_password(password, user.password):

            return Response(error)

    except CustomUser.DoesNotExist:
        user = None
        return Response(error)

    # serializers
    serializer = LoginSerializers(user)
    return Response(serializer.data)
 


#signup view

@api_view(['POST'])
def signup(request):
    email = request.data['email']
    user = CustomUser.objects.filter(email=email).exists()
    
    if not user: #user is False
        # print(user)
        request.data['password'] = make_password(request.data['password'])
        user = CustomUser(**request.data) #request data to user 
        
        # user.get('password') = make_password(user.get('password'))
        
        user.save() #saving user
        serializer = SignupSerializers(user)
        custom_serializer = serializer.data
        custom_serializer["msg"] = "success !" 
        return Response(custom_serializer, status=status.HTTP_201_CREATED)
    # print(user)

    return Response({'msg':'failure !','possible cause':'email already used'})

