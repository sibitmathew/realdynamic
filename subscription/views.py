from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscription
from subscription.models import Subscription
from subscription.serializer import SubscriptionSerializer
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response

# Create your views here.
# Get all subscriptions
def get_subscriptions(request, sub_id = ''):
    if request.method == 'GET':
        if(sub_id == ''):
            subscribers = Subscription.objects.filter().values()
        else:
            subscribers = Subscription.objects.filter(id=sub_id).values()
    return JsonResponse({"subscribers": list(subscribers)})

#Submit subscription
@csrf_protect
def add_subscription(request):
    #subscription_form = Subscription(request.POST or None)
    if request.method == 'POST' and request.is_ajax():
        serializer = SubscriptionSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": "201", "response": "Success", "msg": "Successfully Created",})
        else:
            return JsonResponse({"code": "401", "response": "Error", "msg": "Invalid request", "reason": serializer.errors})
    else:
        return JsonResponse({"code":"400","response": "Error","msg":"Bad request","reason":["Invalid request"]})

