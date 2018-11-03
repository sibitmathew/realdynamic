from django.db import models
from icobase.models import BaseModel

# Create your models here.


# Create your models here.
class Slider(BaseModel):

    slider_name = models.CharField(max_length=40)
    the_problem = models.TextField()
    the_solution = models.TextField()
    slider_image = models.FileField(upload_to='slider_images', null=False, blank=False)

    def __str__(self):
        return self.slider_name
