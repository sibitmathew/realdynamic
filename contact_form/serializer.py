from contact_form.models import ContactForm
from rest_framework import serializers


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ('contact_reason', 'contact_name', 'address', 'email', 'phone_number', 'message')
