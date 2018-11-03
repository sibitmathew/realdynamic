from django.db import models
from icobase.models import BaseModel

# Create your models here.
class Ourfocus(BaseModel):
    title = models.CharField(max_length=40)
    description = models.TextField()
    icon_image = models.FileField(upload_to='focus_icons')


    def __str__(self):
        return self.title