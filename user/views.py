from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import Http404
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


def signin(request):
    if request.user.is_authenticated:
        raise PermissionDenied
    else:
        next_url = request.GET.get('next', 'index')

        if request.method == "POST":
            # 아이디 비번 입력 X
            if not all(i in request.POST for i in ('userId', 'password')):
                return render(request, "signin.html", {
                    "message": "아이디와 비밀번호를 입력 해 주세요",
                    "next_url": next_url,
                })
            user = authenticate(username=request.POST['userId'], password=request.POST['password'])

            # 로그인 성공 / 실패
            if user is not None:
                auth = login(request, user)
                return redirect(next_url)
            else:
                return render(request, "signin.html", {
                    "message": "로그인에 실패 했습니다. 아이디와 비밀번호를 확인 해 주세요",
                    "next_url": next_url,
                })
        # 일반
        else:
            return render(request, "signin.html", {
                "message": "로그인 해 주세요",
                "next_url": next_url
            })



def MyLogout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("/")



def lists(request, page=1):
    queryset = Profile.objects.order_by('-stuNo')[(page-1)*10:page*10]
    UserNumber = Profile.objects.all().count()
    return render(request, 'userList.html', {
        'queryset': queryset,
        'pageNum': ((UserNumber - 1) // 5) + 1
    })


def info(request, id):
    try:
        profile = Profile.objects.get(user_id=id)
        return render(request, 'userInfo.html', {'profile': profile})
    except Profile.DoesNotExist:
        raise Http404()



def modify(request):
    return


def verify(request):
    return

