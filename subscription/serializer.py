from subscription.models import Subscription
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('subscriber_fname', 'subscriber_lname', 'email')
        extra_kwargs = {'subscriber_lname': {'required': False}}
