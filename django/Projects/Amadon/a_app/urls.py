from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('amadon/',views.amadon),
    path('amadon/buy',views.buy),
    
    # path('name',views.red)
    ]