from django.shortcuts import render
from post.models import PostNotice, PostActivity, PostShare, PostFree


def index(request):
    activities = PostActivity.objects.filter(parent=None).order_by('-id')[:8]
    notices = PostNotice.objects.filter(parent=None).order_by('-id')[:5]
    shares = PostShare.objects.filter(parent=None).order_by('-id')[:5]
    frees = PostFree.objects.filter(parent=None).order_by('-id')[:5]
    return render(request, 'index.html', {
        'activities': activities,
        'notices': notices,
        'shares': shares,
        'frees': frees
    })


def policy(request):
    return render(request, 'policy.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


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
