from django.urls import path
from . import views

urlpatterns = [
    path('', views.bestiary_list, name = 'bestiary_list'),
    path('add/', views.add_monster, name = 'add_monster'),
]