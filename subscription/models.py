from django.db import models
from icobase.models import BaseModel


# Create your models here.
class Subscription(BaseModel):

    subscriber_fname = models.CharField(max_length=80)
    subscriber_lname = models.CharField(max_length=80)
    email = models.EmailField(unique= True)

    def __str__(self):
        return self.subscriber_fname