from django.urls import path
from . import views

urlpatterns = [
    path('<str:boardName>/', views.detail, name='detail'),
]