from django.urls import path
from . import views

urlpatterns = [
		path('', views.login),
        path('reg_validate', views.reg_validate),
		path('login_validate', views.login_validate),
		path('wall', views.wall),
		path('logout', views.logout),
		path('message', views.post_message),
		path('comment/<int:msg_id>', views.post_comment)
  
	]