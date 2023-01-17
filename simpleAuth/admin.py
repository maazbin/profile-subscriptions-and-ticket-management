# from dataclasses import field
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser



'''
This is custom user class where we can add fields which are not by default provided 
in django user model. This user model can be accessed throu authApp
'''
# @admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = (
        'password',
        'id',
        'email', 
        'first_name', 
        'last_name',
        'creation_date',
        'is_staff',

        )

    
admin.site.register(CustomUser, CustomUserAdmin)