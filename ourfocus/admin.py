from django.contrib import admin
from .models import Ourfocus

class FocusAdmin(admin.ModelAdmin):
    save_as = True
# Register your models here.
admin.site.register(Ourfocus,FocusAdmin)
