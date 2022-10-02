from django.urls import path
from . import views
from i_app.models import Book,Author 
urlpatterns = [path('', views.showbook),
path('books/<int:idbook>', views.bookpage),
path('authors', views.showauthor),
path('authors/<int:idauthor>', views.authorpage),
path('addbook' ,views.addbook),
path('authors/addauthor' ,views.addauthor),
path('',views.addbooksforauthors),
path('addauthor/<int:id>',views.addauthorsforbook)
]