from django.contrib import admin
from .models import Subscription

class SubAdmin(admin.ModelAdmin):
    list_display = ('subscriber_fname', 'subscriber_lname', 'email')
    search_fields = ('subscriber_fname', 'subscriber_lname', 'email')
    list_filter = ('created','modified')
    ordering = ('-created',)
    list_per_page = 10

# Register your models here.
admin.site.register(Subscription, SubAdmin)
