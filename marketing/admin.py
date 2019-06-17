from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from marketing.models import News

class NewsAdminForm(forms.ModelForm):
    NEWS_TYPE = (
        ('Promo', 'Promotion'),
        ('Normal', 'Normal'),
        ('Project', 'Project'),
    )
    content = forms.CharField(widget=CKEditorUploadingWidget())
    category = forms.ChoiceField(choices=NEWS_TYPE)
    class Meta:
        model = News
        fields = ('title', 'category', 'news_image', 'content', 'display_text')

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

admin.site.register(News, NewsAdmin)
