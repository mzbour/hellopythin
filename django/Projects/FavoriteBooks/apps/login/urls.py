from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('reg_validate', views.reg_validate),
		path('login_validate', views.login_validate),
		path('home', views.home),
		path('logout', views.logout),
		path('addbook/<int:userid>',views.addbook),
		path('books/<int:bid>',views.showbook),
		path('update/<int:fid>',views.update),
		path('addfavbook/<int:bid>',views.addfavbook),
		path('book/<int:mid>',views.showbookwithfirstuser),


	]