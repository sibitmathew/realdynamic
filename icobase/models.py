from django.db import models
from django.db.models import signals
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
