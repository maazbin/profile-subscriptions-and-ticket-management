from rest_framework import serializers
from subscriptions.models import  Subscription,SubscriptionType




class SubscriptionTypeSerializers(serializers.ModelSerializer):

    class Meta :
        model = SubscriptionType
        fields = ['name']


class SubscriptionSerializers(serializers.ModelSerializer):

    subscription_type = serializers.StringRelatedField()

    class Meta :
        model = Subscription
        fields = [
            'serial_no',
            'date_of_purchase',
            'date_of_expiry',
            'subscription_type'
        ]




class UpdateSubscriptionSerializers(serializers.ModelSerializer):

    subscription_type = serializers.StringRelatedField( )
    
    class Meta :
        model = Subscription
        fields = [
            'serial_no',
            'date_of_purchase',
            'date_of_expiry',
            'subscription_type',
            # 'user'
        ]

        extra_kwargs = {
            'date_of_purchase':{'required': False},
            'date_of_expiry':{'required': False},
            'subscription_type':{'required': False},

        }