from django.shortcuts import render

# Create your views here.


def signup(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            error_dict = {
                "status_code": 403,
                "message_title": "403 Error",
                "message_context": "잘못 된 요청입니다."
            }
            return render(request, 'error.html', {}, status=403)

        render(request, 'signup.html', )
    else:
        error_dict = {
            "status_code": 405,
            "message_title": "405 Error",
            "message_context": "잘못 된 요청 방식입니다."
        }
        return render(request, 'error.html', {}, status=405)


def login(request):
    return


def lists(request):
    return


def info(request):
    return


def modify(request):
    return


def verify(request):
    return

