from django.urls import path
from . import views

urlpatterns = [
    path('', views.WeaponListView.as_view(), name = 'weapon_list'),
    path('add/', views.WeaponCreateView.as_view(), name = 'weapon_create'),
    path('<int:pk>/edit/', views.WeaponUpdateView.as_view(), name = 'weapon_edit'),
    path('<int:pk>/delete/', views.WeaponDeleteView.as_view(), name = 'weapon_delete'),
]