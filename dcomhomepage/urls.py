"""dcomhomepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dcomhomepage import views


urlpatterns = [
    path('', views.index, name='index'),
    path('policy/', views.policy, name='policy'),
    path('privacy/', views.privacy, name='privacy'),
    path('admin/', admin.site.urls, name='admin'),
    path('board/', include('board.urls'), name='board'),
    path('file/', include('file.urls'), name='file'),
    path('info/', include('info.urls'), name='info'),
    path('post/', include('post.urls'), name='post'),
    path('user/', include('user.urls'), name='user'),
    path('api/', include('api.urls'), name='api'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


