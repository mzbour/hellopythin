from django.urls import path
from . import views

urlpatterns=[path('',views.show),
path('m',views.show1)]
