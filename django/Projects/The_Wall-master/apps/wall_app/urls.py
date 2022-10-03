from django.conf.urls import url
from . import views, models

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^message$', views.post_message),
    url(r'^comment/(?P<msg_id>\d+)$', views.post_comment),
    url(r'^destroy$', views.destroy),
]