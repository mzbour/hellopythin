from django.urls import path
from . import views
urlpatterns=[
 path('', views.display1),path('result/',views.display2)]
 