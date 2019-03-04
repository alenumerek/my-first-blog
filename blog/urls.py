from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_list, name="post_list"),  #ścieżka, sam adres 127:1:0:0:80000, widok zdefiniowany blog_list, nazwa, post_list
]