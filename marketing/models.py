from django.db import models
from icobase.models import BaseModel


from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(BaseModel):
    NEWS_TYPE = (
        ('Promo', 'Promotion'),
        ('Normal', 'Normal'),
        ('Project', 'Project'),
    )
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=40, choices=NEWS_TYPE)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title