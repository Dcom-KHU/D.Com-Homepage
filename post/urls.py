from django.urls import path
from . import views
urlpatterns = [
    path('<str:boardName>/<int:id>/', views.detail, name='detail'),
    path('<str:boardName>/write/', views.write, name='write'),
]