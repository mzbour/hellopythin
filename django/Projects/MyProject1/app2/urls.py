from django.urls import path
from . import views

urlpatterns=[
 path('', views.display1),
 path('display1/', views.display2),
 path('display1/display2/', views.display3)
]