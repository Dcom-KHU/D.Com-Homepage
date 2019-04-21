from django.urls import path
from . import views

urlpatterns = [
    path('notice/<int:post_id>/', views.notice_detail, name='notice_detail'),
    path('notice/list/', views.notice_list, name='notice_list'),
    path('notice/list/<int:page>/', views.notice_list, name='notice_lists'),
    path('notice/write/', views.notice_post, name='notice_post'),
    path('notice/write/<int:parents>', views.notice_post, name='notice_comment_post'),
    path('free/<int:post_id>/', views.free_detail, name='free_detail'),
    path('free/list/', views.free_list, name='free_list'),
    path('free/list/<int:page>/', views.free_list, name='free_lists'),
    path('free/write/', views.free_post, name='free_post'),
    path('free/write/<int:parents>', views.free_post, name='free_comment_post'),
    path('jokbo/<int:post_id>/', views.jokbo_detail, name='jokbo_detail'),
    path('jokbo/list/', views.jokbo_list, name='jokbo_list'),
    path('jokbo/list/<int:page>/', views.jokbo_list, name='jokbo_lists'),
    path('jokbo/write/', views.jokbo_post, name='jokbo_post'),
    path('jokbo/write/<int:parents>', views.jokbo_post, name='share_comment_post'),
    path('share/<int:post_id>/', views.share_detail, name='share_detail'),
    path('share/list/', views.share_list, name='share_list'),
    path('share/list/<int:page>/', views.share_list, name='share_lists'),
    path('share/write/', views.share_post, name='share_post'),
    path('share/write/<int:parents>', views.share_post, name='share_comment_post'),
]