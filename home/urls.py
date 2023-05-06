from django.contrib import admin
from django.urls import path
from home.views import home, about, chatAPI

urlpatterns = [
    path('chat', home, name='home'),
    path('about', about, name='about'),
    path('api', chatAPI, name='chatAPI'),
]
