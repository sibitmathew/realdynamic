from django.conf.urls import include, url
from subscription import views

urlpatterns = [
    url(r'^details/get/$', views.get_subscriptions),
    url(r'^details/get/(?P<sub_id>\w+)/$', views.get_subscriptions),
    url(r'^new/add/$', views.add_subscription),
]