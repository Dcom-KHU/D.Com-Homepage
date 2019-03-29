from django.shortcuts import render
from django.core.exceptions import PermissionDenied


def signup(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            raise PermissionDenied
        else:
            return render()

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

