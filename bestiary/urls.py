from django.urls import path
from . import views

urlpatterns = [
    path('', views.bestiary_list, name = 'bestiary_list'),
    path('add/', views.add_monster, name = 'add_monster'),
    path('details/<int:pk>/', views.monster_details, name = 'monster_details'),
    path('edit/<int:pk>/', views.edit_monster, name = 'edit_monster'),
    path('delete/<int:pk>/', views.delete_monster, name = 'delete_monster'),
]