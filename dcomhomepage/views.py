from django.shortcuts import render
from post.models import PostNotice

def index(request):
    name = '오윤석'
    posts = PostNotice.objects.all()
    return render(request, 'index.html', {'name': name, 'posts': posts})
