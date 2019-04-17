from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.MyLogout, name='logout'),
    path('list/', views.lists, name='list'),
    path('list/<int:page>/', views.lists, name='lists'),
    path('<int:id>/', views.info, name='info'),
    path('edit/', views.edit, name='verify'),
    path('welcome/', views.welcome, name='welcome'),
    path('changePassword/', views.changePassword, name='change_password'),
    path('verify/<int:id>', views.verify, name='verify')
]