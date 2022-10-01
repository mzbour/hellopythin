from django.urls import path
from . import views
from t_app.models import *
urlpatterns = [
path('', views.first),
path('shows', views.show),
path('shows/<int:showid>/edit',views.edit),
path('shows/new',views.createshow),
path('shows/<int:idm>',views.tv),
path('shows/<int:rid>',views.returntotv),
path('act',views.myproplem),
path('preeditm/<int:myid>',views.preedit),
# path('sh/<int:fid>',views.editd),
path('delete/<int:mid>',views.delete),

]