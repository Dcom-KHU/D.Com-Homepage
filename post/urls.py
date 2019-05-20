from django.urls import path
from post import views

urlpatterns = [
    path('notice/<int:post_id>/', views.notice_detail, name='notice_detail'),
    path('notice/comments/<int:post_id>/', views.notice_comment, name='notice_comment'),
    path('notice/list/', views.notice_list, name='notice_list'),
    path('notice/list/<int:page>/', views.notice_list, name='notice_lists'),
    path('notice/write/', views.notice_post, name='notice_post'),
    path('notice/delete/', views.notice_delete, name='notice_delete'),
    path('activity/<int:post_id>/', views.activity_detail, name='activity_detail'),
    path('activity/comments/<int:post_id>/', views.activity_comment, name='activity_comment'),
    path('activity/list/', views.activity_list, name='activity_list'),
    path('activity/list/<int:page>/', views.activity_list, name='activity_lists'),
    path('activity/write/', views.activity_post, name='activity_post'),
    path('activity/delete/', views.activity_delete, name='activity_delete'),
    path('free/<int:post_id>/', views.free_detail, name='free_detail'),
    path('free/comments/<int:post_id>/', views.free_comment, name='free_comment'),
    path('free/list/', views.free_list, name='free_list'),
    path('free/list/<int:page>/', views.free_list, name='free_lists'),
    path('free/write/', views.free_post, name='free_post'),
    path('free/delete/', views.free_delete, name='free_delete'),
    path('study/<int:post_id>/', views.study_detail, name='study_detail'),
    path('study/comments/<int:post_id>/', views.study_comment, name='study_comment'),
    path('study/list/', views.study_list, name='study_list'),
    path('study/list/<int:page>/', views.study_list, name='study_lists'),
    path('study/write/', views.study_post, name='study_post'),
    path('study/join/<int:post_id>', views.study_join, name='study_join'),
]