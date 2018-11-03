from django.conf.urls import url, include

from contact_form import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^contact/$', views.new_contact)
]