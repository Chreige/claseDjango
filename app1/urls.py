from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vista1/', views.vista1),
]