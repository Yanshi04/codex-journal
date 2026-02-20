from django.urls import path
from .views import home_page
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
]