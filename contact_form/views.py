from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from contact_form.models import ContactForm
from contact_form.serializer import ContactFormSerializer
from django.http import HttpResponse
import simplejson as json

@csrf_exempt
@api_view(['POST'])
def new_contact(request):
    if request.method == 'POST':
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
