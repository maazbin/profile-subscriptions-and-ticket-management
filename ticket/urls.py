from django.urls import path
from ticket import views  #importing views from subscriptions

urlpatterns = [
    # path('hello/',views.hello,name='hello'),
    path('get-ticket/<str:uuid>/',views.ticket_view,name='get-ticket'),
    path('create-ticket/',views.ticket_view,name='get-ticket'),
    path('update-ticket/',views.ticket_view,name='get-ticket'),
    path('delete-ticket/<str:uuid>/',views.ticket_view,name='get-ticket'),
    path('get-all-tickets/<str:pk>/',views.get_all_tickets,name='get-all-ticket'),

]