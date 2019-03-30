from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from user.models import Profile
from user.form import UserSignUpForm


def signup(request):
    if request.user.is_authenticated:
        raise PermissionDenied
    if request.method == "GET":
        form = UserSignUpForm()
        message = '회원 가입 폼을 입력 해 주세요'
        return render(request, 'signup.html', {
            "message": message
        })
    elif request.method == "POST":
        require_keys = ('userId', 'password', 'first_name', 'last_name', 'email', 'stuNo', 'phoneNum')
        if all(i in request.POST for i in require_keys):
            userobj = User.objects.create(
                username=request.POST['userId'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email']
            )
            profileobj = Profile.objects.create(
                user=userobj,
                stuNo=request.POST['stuNo'],
                phoneNum=request.POST['phoneNum'],
                github=request.POST.get('github', '')
            )
            login(request, userobj)
            return redirect("/user/welcome/")
        else:
            message = '오류가 발생했습니다.'
            return render(request, 'signup.html', {
                "message": message
            })


def welcome(request):
    if not request.user.is_authenticated:
        return redirect("/user/signin/")
    else:
        return render(request, "congratuation.html")


def logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("/user/signin/")


def lists(request):
    return


def info(request):
    return


def modify(request):
    return


def verify(request):
    return

