from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('people_detail/', views.people_details),
]
