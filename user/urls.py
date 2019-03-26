from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('list/', views.lists, name='lists'),
    path('<int:id>/', views.info, name='info'),
    path('verify/', views.verify, name='verify'),
]