from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.safety),
    path('lpg/', views.lpg),
    path('temp/', views.temp),
]