from django.urls import path
from . import views

urlpatterns = [
    path('', views.showme),path('show', views.hello)
    ]