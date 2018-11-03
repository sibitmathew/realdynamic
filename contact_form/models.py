from django.db import models
from icobase.models import BaseModel


# Create your models here.
class ContactForm(BaseModel):
    REASON_TYPE = (
        ('A','Reason 1'),
        ('B', 'Reason 2'),
    )
    contact_reason = models.CharField(max_length=50, choices=REASON_TYPE )
    contact_name = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.contact_name