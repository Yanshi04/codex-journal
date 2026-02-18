from django.urls import path
from .views import create_profile

urlpatterns = [path('create/', create_profile, name='create profile'),]