from django.urls import path
from . import views

urlpatterns=[path('',views.index),
path('name/', views.numme),
path('blogs/', views.root),
path('blog/', views.indexm),
path('blogs/new/',views.new),
path('blogs/create/',views.create),
path('blogs/<int:number>/',views.show),
path('blogs/<int:number>/edit/',views.edit),
path('/blogs/<int:num>/delete',views.destroy)

]