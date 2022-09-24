from django.urls import path     
from . import views
urlpatterns = [
    path('', views.display),	
    path('destroy/',views.destroy)
]