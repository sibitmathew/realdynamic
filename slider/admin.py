from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    save_as = True

# Register your models here.
admin.site.register(Slider,SliderAdmin)