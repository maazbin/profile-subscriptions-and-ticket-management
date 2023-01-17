from rest_framework import serializers
from ticket.models import IssueType,Ticket




class IssueTypeSerializers(serializers.ModelSerializer):

    class Meta :
        model = IssueType
        fields = ['name']


class TicketSerializers(serializers.ModelSerializer):

    issue_type = serializers.StringRelatedField()

    class Meta :
        model = Ticket
        fields = [
            'ticket_id',
            'user_id',
            'issue_type',
            'ticket_date',
            'ticket_description'
        ]



class UpdateTicketSerializers(serializers.ModelSerializer):

    issue_type = serializers.StringRelatedField()

    class Meta :
        model = Ticket
        fields = [
            'ticket_id',
            # 'user_id',
            'issue_type',
            'ticket_date',
            'ticket_description'
        ]
        extra_kwargs = {
            'ticket_date':{'required': False},
            'ticket_description':{'required': False},
            'issue_type':{'required': False},

        }



