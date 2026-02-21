from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowAllMonsters.as_view(), name='bestiary_list'),
    path('add/', views.CreateMonsterPage.as_view(), name='add_monster'),
    path('details/<int:pk>/', views.MonsterDetailsPage.as_view(), name='monster_details'),
    path('edit/<int:pk>/', views.EditMonsterPage.as_view(), name='edit_monster'),
    path('delete/<int:pk>/', views.DeleteMonsterPage.as_view(), name='delete_monster'),
]