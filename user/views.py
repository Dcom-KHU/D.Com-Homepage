from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import EmailMessage
from user.models import Profile
import string
import random


def signupForm(request):
    if request.user.is_authenticated:
        raise PermissionDenied

    if request.method == "POST":
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
            return render(request, 'signupForm.html', {
                "message": message
            })
    else:
        message = '회원 가입 폼을 입력 해 주세요'
        return render(request, 'signupForm.html', {
            "message": message
        })


def welcome(request):
    if not request.user.is_authenticated:
        return redirect("/user/signin/")
    else:
        return render(request, "congratuation.html")


def signup(request):
    if request.user.is_authenticated:
        raise PermissionDenied
    else:
        return render(request, "signup.html")


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


@login_required
def edit(request):
    profile = Profile.objects.get(user=request.user)
    if Profile is None:
        status_code = 500
        return render(request, 'error.html', {
            'status_code': status_code,
            'message_title': '서버 오류가 발생했습니다.',
            'message_context': '프로필을 불러 올 수 없습니다.'
        }, status=status_code)

    if request.method == "POST":
        require_keys = ('password', 'email', 'phoneNum')
        if all(i in request.POST for i in require_keys):
            if request.user.check_password(request.POST['password']):
                request.user.email = request.POST['email']
                request.user.save()
                profile.phoneNum = request.POST['phoneNum']
                profile.save()
                return render(request, 'edit.html', {
                    'message': '변경이 성공적으로 적용 되었습니다.',
                    'profile': profile
                })
            else:
                return render(request, 'edit.html', {
                    'message': '비밀 번호가 틀렸습니다, 다시 입력 해 주세요',
                    'profile': profile
                })
        else:
            return render(request, 'edit.html', {
                'message': '필수 항목을 입력 해 주세요',
                'profile': profile
            })
    else:
        return render(request, 'edit.html', {
            'message': '유저 내용을 수정해 주세요',
            'profile': profile
        })


@login_required
def verify(request, id):
    profile = Profile.objects.get(user=request.user)
    page = request.GET.get('page', '1')
    if profile.isVerified == 2:
        try:
            verified_profile = Profile.objects.get(user_id=id)
            verified_profile.isVerified = 1
            verified_profile.save()
            return redirect('/user/list/{}'.format(page))
        except Profile.DoesNotExist:
            return render(request, 'error.html', {
                'status_code': 500,
                'message_title': '서버 오류가 발생했습니다.',
                'message_context': '프로필을 불러 올 수 없습니다.'
            }, status=500)
    else:
        raise PermissionDenied


@login_required
def changePassword(request):
    if request.method == "POST":
        if not all(i in request.POST for i in ('current', 'wish')):
            return render(request, 'changePassword.html', {
                'message': '현재 비밀번호, 변경 할 비밀번호 모두를 입력 해 주세요.'
            })
        elif request.user.check_password(request.POST['current']):
            request.user.set_password(request.POST['wish'])
            request.user.save()
            return redirect("/user/signin/")
        else:
            return render(request, 'changePassword.html', {
                'message': '현재 비밀번호가 틀렸습니다. 다시 입력 해 주세요'
            })
    else:
        return render(request, 'changePassword.html', {
            'message': '변경 할 비밀 번호를 입력 해 주세요.'
        })


def findId(request):
    if request.user.is_authenticated:
        raise PermissionDenied

    if request.method == "POST":
        require_keys = ('email',)
        if all(i in request.POST for i in require_keys):
            try:
                user = User.objects.get(email=request.POST['email'])
                username = user.username

                for i in range(len(username) // 2, len(username)):
                    username[i] = '*'

                return render(request, 'result.html', {
                    'message': '{} 와 연결된 계정의 ID는 다음과 같습니다.'.format(request.POST['email']),
                    'result': username
                })
            except User.DoesNotExist:
                return render(request, 'findId.html', {
                    'message': '일치하는 아이디가 없습니다.'
                })
        else:
            return render(request, 'findId.html', {
                'message': '이메일을 입력 해 주세요.'
            })
    else:
        return render(request, 'findId.html', {
            'message': '이메일을 통해 아이디를 찾습니다.'
        })


def findPassword(request):
    if request.user.is_authenticated:
        raise PermissionDenied

    if request.method == "POST":
        require_keys = ('userId', 'email')
        if all(i in request.POST for i in require_keys):
            try:
                user = User.objects.get(email=request.POST['email'], username=['userId'])
                new_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                user.set_password(new_password)
                EmailMessage('D.Com 홈페이지 비밀번호가 변경 되었습니다.', '귀하의 변경된 비밀번호는 {} 입니다. \n비밀번호 변경을 신청하지 않으셨다면 관리자에게 문의 주세요.'.format(new_password), to=[user.email])
                return render(request, 'result.html', {
                    'message': '귀하의 이메일, {} 로 변경된 비밀 번호가 전송 되었습니다.'.format(user.email)
                })
            except User.DoesNotExist:
                return render(request, 'findPassword.html', {
                    'message': '입력 하신 정보가 일치 하지 않습니다, 다시 입력 해 주세요.'
                })

    return render(request, 'findPassword.html', {
        'message': '임시 비밀번호 발급을 위해 아이디와 이메일을 입력 해 주세요.'
    })
