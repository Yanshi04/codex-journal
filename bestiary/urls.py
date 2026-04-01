from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.ShowAllMonsters.as_view(), name='bestiary_list'),
    path('add/', views.CreateMonsterPage.as_view(), name='add_monster'),
    path('details/<int:pk>/', views.MonsterDetailsPage.as_view(), name='monster_details'),
    path('edit/<int:pk>/', views.EditMonsterPage.as_view(), name='edit_monster'),
    path('delete/<int:pk>/', views.DeleteMonsterPage.as_view(), name='delete_monster'),
    path('download/', views.DownloadCSVView.as_view(), name='download_csv'),
    path('api/monsters/', api.MonsterListCreateAPI.as_view(), name='api-monster-list'),
    path('api/monsters/<int:pk>/', api.MonsterDetailAPI.as_view(), name='api-monster-detail'),
]