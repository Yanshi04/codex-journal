from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestListView.as_view(), name ='quest_list'),
    path('add/', views.QuestCreateView.as_view(), name ='quest_create'),
    path('edit/<int:pk>/', views.QuestEditView.as_view(), name='quest_edit'),
    path('delete/<int:pk>/', views.QuestDeleteView.as_view(), name='quest_delete'),
]