from django.urls import path
from subscriptions import views  #importing views from subscriptions

urlpatterns = [
    path('hello/',views.hello,name='hello'),
    path('get-sub/<str:uuid>/',views.subscriptions_method,name='get-sub'),
    path('create-sub/',views.subscriptions_method,name='get-sub'),
    path('update-sub/',views.subscriptions_method,name='get-sub'),
    path('delete-sub/<str:uuid>/',views.subscriptions_method,name='get-sub'),
    path('get-all-sub/<str:pk>/',views.get_all_subscription,name='get-all-sub'),

]