from django.conf.urls import url, include

from marketing import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^(?P<blog_id>\d+)/$', views.blog, name='blog')
]