from django.urls import path
from simpleAuth import views  #importing views from simpleAuth

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),

]