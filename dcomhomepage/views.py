from django.shortcuts import render
from post.models import PostNotice


def index(request):
    name = '오윤석'
    posts = PostNotice.objects.filter(parent=None).order_by('-id')
    return render(request, 'index.html', {'name': name, 'posts': posts})


"""
def page404(request):
    error_dict = {
        "status_code": 404,
        "message_title": "페이지를 찾을 수 없습니다.",
        "message_context": "404 Error - Page Not Found"
    }
    return render(request, 'error.html', error_dict, status=404)


def page400(request):
    error_dict = {
        "status_code": 400,
        "message_title": "잘못된 요청입니다.",
        "message_context": "400 Error - Bad Request"
    }
    return render(request, 'error.html', error_dict, status=400)


def page403(request):
    error_dict = {
        "status_code": 403,
        "message_title": "금지된 요청입니다.",
        "message_context": "403 Error - Forbidden"
    }
    return render(request, 'error.html', error_dict, status=403)


def page500(request):
    error_dict = {
        "status_code": 500,
        "message_title": "서버 에러입니다.",
        "message_context": "500 Error - Internal Server Error"
    }
    return render(request, 'error.html', error_dict, status=500)
"""
