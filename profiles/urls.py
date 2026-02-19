from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_profile, name='profile_create'),
    path('details/', views.profile_details, name='profile_details'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('delete/', views.profile_delete, name='profile_delete'),
]