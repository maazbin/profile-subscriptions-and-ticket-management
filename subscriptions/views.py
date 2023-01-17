
# Django rest framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from subscriptions.serializers import SubscriptionSerializers,UpdateSubscriptionSerializers
from subscriptions.models import Subscription,SubscriptionType
from simpleAuth.models import CustomUser

@api_view(['GET'])
def hello(request):
    return Response({'msg' : 'Hello , world'})


@api_view(['POST', 'GET','PUT','DELETE'])
def subscriptions_method(request,uuid=None):
    """
    Retrieve, update or delete a code subscriptions.
    
    """

    if request.method == 'POST':
        
        try:
            user = CustomUser.objects.get(id = request.data['user'])
        except CustomUser.DoesNotExist:
            return Response({'msg' : 'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            type = SubscriptionType.objects.get(name = request.data['subscription_type'])
        except Subscription.DoesNotExist:
            return Response({'msg' : 'subscription type not found'}, status=status.HTTP_400_BAD_REQUEST)    

        data = {
            # 'date_of_purchase': request.data['date_of_purchase'],
            # 'date_of_expiry': request.data['date_of_expiry'],
            'user' : user,
            'subscription_type' : type,
        }

        

        subs = Subscription(**data)
        subs.save()
        
        serializer = SubscriptionSerializers(subs)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    elif request.method == 'PUT':
        
        
        try:
            subs = Subscription.objects.get(serial_no = request.data['serial_no'])
        except Subscription.DoesNotExist:
            return Response({'msg' : 'serial number not found'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('subscription_type'):
            
            try:
                type = SubscriptionType.objects.get(name = request.data.get('subscription_type'))
            except SubscriptionType.DoesNotExist:
                return Response({'msg': 'subscription type not found'}, status=status.HTTP_400_BAD_REQUEST)    

        
            subs.subscription_type = type
        
        

        serializer = UpdateSubscriptionSerializers(subs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

           


    try:
        subs = Subscription.objects.get(serial_no=uuid)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = SubscriptionSerializers(subs)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        subs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
   


# gets all subs of a user
@api_view(['GET'])
def get_all_subscription(request,pk):
    
    
    subs = Subscription.objects.filter(user = pk)

    serializer = SubscriptionSerializers(subs,many = True)
    return Response({"subscription" : serializer.data}) 