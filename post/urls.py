from django.urls import path
from post import views

urlpatterns = [
    path('notice/<int:post_id>/', views.notice_detail, name='notice_detail'),
    path('notice/comments/<int:post_id>/', views.notice_comment, name='notice_comment'),
    path('notice/list/', views.notice_list, name='notice_list'),
    path('notice/list/<int:page>/', views.notice_list, name='notice_lists'),
    path('notice/write/', views.notice_post, name='notice_post'),
    path('study/<int:post_id>/', views.study_detail, name='study_detail'),
    path('study/comments/<int:post_id>/', views.study_comment, name='study_comment'),
    path('study/list/', views.study_list, name='study_list'),
    path('study/list/<int:page>/', views.study_list, name='study_lists'),
    path('study/write/', views.study_post, name='study_post'),
    path('study/join/<int:post_id>', views.study_join, name='study_join'),
]