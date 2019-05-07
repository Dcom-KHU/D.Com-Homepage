from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice_upload, name='notice_upload'),
    path('activity/', views.activity_upload, name='activity_upload'),
    path('free/', views.free_upload, name='free_upload'),
    path('share/', views.share_upload, name='share_upload'),
    path('study/', views.study_upload, name='study_upload'),
    path('jokbo/', views.jokbo_upload, name='jokbo_upload')
]