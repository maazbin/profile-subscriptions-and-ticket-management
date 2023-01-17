
# Django rest framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ticket.serializers import TicketSerializers,IssueTypeSerializers,UpdateTicketSerializers
from ticket.models import Ticket,IssueType
from simpleAuth.models import CustomUser

@api_view(['GET'])
def hello(request):
    return Response({'msg' : 'Hello , world'})


@api_view(['POST', 'GET','PUT','DELETE'])
def ticket_view(request,uuid=None):
    """
    Retrieve, update or delete a code subscriptions.
    
    """

    if request.method == 'POST':
        
        try:
            user_id = CustomUser.objects.get(id = request.data['user_id'])
        except CustomUser.DoesNotExist:
            return Response({'msg': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            type = IssueType.objects.get(name = request.data['issue_type'])
        except IssueType.DoesNotExist:
            return Response({'msg': 'issue type not found'}, status=status.HTTP_400_BAD_REQUEST)    

        data = {
            # 'ticket_date': request.data['ticket_date'],
            'ticket_description': request.data['ticket_description'],
            'user_id' : user_id,
            'issue_type' : type,
        }

        

        ticket = Ticket(**data)
        ticket.save()
        
        serializer = TicketSerializers(ticket)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    elif request.method == 'PUT':
        
      

        try:
            ticket = Ticket.objects.get(ticket_id = request.data['ticket_id'])
        except Ticket.DoesNotExist:
            return Response({'msg': 'ticket not found'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('issue_type'):
            
            try:
                type = IssueType.objects.get(name = request.data.get('issue_type'))
            except IssueType.DoesNotExist:
                return Response({'msg': 'issue type not found'}, status=status.HTTP_400_BAD_REQUEST)    

        # data = {
        #     'date_of_purchase': request.data['date_of_purchase'],
        #     'date_of_expiry': request.data['date_of_expiry'],
        #     # 'serial_no' : request.data['serial_no'],
        #     'subscription_type' : type,
        #     # 'user' : user,
        # }

        
            ticket.issue_type = type
        # else :
        
        # subs.save()

        serializer = UpdateTicketSerializers(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer = SubscriptionSerializers(subs)
        # return Response(serializer.data,status=status.HTTP_201_CREATED)
    


    try:
        ticket = Ticket.objects.get(ticket_id=uuid)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = TicketSerializers(ticket)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
   
    
# gets all tickets of a user
@api_view(['GET'])
def get_all_tickets(request,pk):
    
    
    ticket = Ticket.objects.filter(user_id = pk)

    serializer = TicketSerializers(ticket,many = True)
    return Response({"tickets" : serializer.data}) 