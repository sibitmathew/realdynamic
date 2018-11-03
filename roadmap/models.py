from django.db import models
from icobase.models import BaseModel

# Create your models here.
class Roadmap(BaseModel):
    ICON_TYPE = (
            ('fa-building', 'Building'),
            ('fa-briefcase', 'Briefcase'),
            ('fa-chart-line', 'Chart'),
            ('fa-city', 'City'),
            ('fa-compass', 'Compass'),
            ('fa-home', 'Home'),
        )
    title = models.CharField(max_length=40)
    year = models.IntegerField(('year'), choices=[(x, str(x)) for x in range(2010,2025)],unique= True)
    icon_type = models.CharField(max_length=40, choices=ICON_TYPE)
    description = models.TextField()
    background_image = models.FileField(upload_to='roadmap_images')


    def __str__(self):
        return self.title