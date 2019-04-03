from django.urls import path
from . import views
urlpatterns = [
    path('notice/<int:post_id>', views.notice_detail, name='notice_detail')
]