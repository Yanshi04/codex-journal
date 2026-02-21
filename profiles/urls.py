from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.MakeProfile.as_view(), name='profile_create'),
    path('details/', views.ViewMyProfile.as_view(), name='profile_details'),
    path('edit/', views.ChangeMyProfile.as_view(), name='profile_edit'),
    path('delete/', views.RemoveMyProfile.as_view(), name='profile_delete'),
]