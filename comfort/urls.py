from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.comfort),
    path('led1', views.led1),
    path('led2', views.led2),
    path('fan', views.fan),
]