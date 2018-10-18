from django.db import models
from icobase.models import BaseModel

# Create your models here.
class TeamMember(BaseModel):
    TEAM_TYPE = (
        ('Core', 'Core Team'),
        ('Advisor', 'Advisor'),
        ('Partner', 'Partner'),
    )
    full_name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    photo = models.FileField(upload_to='member_photo', null=True, blank=True)
    linkedin = models.CharField(max_length=200)
    team = models.CharField(max_length=40, choices=TEAM_TYPE)

    def __str__(self):
        return self.full_name