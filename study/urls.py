from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.study_list, name='list'),
    path('list/<int:page>/', views.study_list, name='lists'),
    path('<int:post_id>/', views.study_detail, name='detail')
]