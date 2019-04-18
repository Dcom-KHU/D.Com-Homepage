from django.urls import path
from . import views

urlpatterns = [
    path('notice/<int:post_id>/', views.notice_detail, name='notice_detail'),
    path('notice/list/', views.notice_list, name='notice_list'),
    path('notice/list/<int:page>/', views.notice_list, name='notice_lists'),
    path('notice/post/', views.notice_post, name='notice_post'),
    path('notice/post/<int:parents>', views.notice_post, name='notice_comment_post'),
    path('free/<int:post_id>/', views.free_detail, name='free_detail'),
    path('free/list/', views.free_list, name='free_list'),
    path('free/list/<int:page>/', views.free_list, name='free_lists'),
    path('free/post/', views.free_post, name='free_post'),
    path('free/post/<int:parents>', views.free_post, name='free_comment_post'),
    path('jokbo/<int:post_id>/', views.jokbo_detail, name='jokbo_detail'),
    path('jokbo/list/', views.jokbo_list, name='jokbo_list'),
    path('jokbo/list/<int:page>/', views.jokbo_list, name='jokbo_lists'),
    path('jokbo/post/', views.jokbo_post, name='jokbo_post'),
    path('jokbo/post/<int:parents>', views.jokbo_post, name='jokbo_comment_post'),
]