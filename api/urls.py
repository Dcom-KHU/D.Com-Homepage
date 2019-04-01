from django.urls import path
from . import views

urlpatterns = [
    path('user/id_check/', views.user_check, name='user_check'),
    path('user/email_check/', views.email_check, name='email_check')
]
