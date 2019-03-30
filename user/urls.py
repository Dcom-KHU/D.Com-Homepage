from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.MyLogout, name='logout'),
    path('list/<int:page>', views.lists, name='lists'),
    path('<int:id>/', views.info, name='info'),
    path('verify/', views.verify, name='verify'),
    path('welcome/', views.welcome, name='welcome')
]