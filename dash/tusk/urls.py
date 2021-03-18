from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.display_login),
    path('register', views.display_register),
    path('home', views.home),
    path('test', views.test),
    path('profile', views.profile),
    path('bookmarks', views.bookmarks),
]