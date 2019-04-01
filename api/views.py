from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def user_check(request):
    """
    유저 체크
    """
    userId = request.data.get('userId')
    if userId is None:
        return Response({"error": "key error"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        userobj = User.objects.get(username=userId)
        return Response({"exists": True})
    except User.DoesNotExist:
        return Response({"exists": False})


@api_view(['POST'])
def email_check(request):
    """
    이메일 체크
    """
    email = request.data.get('email')
    if email is None:
        return Response({"error": "key error"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        userobj = User.objects.get(email=email)
        return Response({"exists": True})
    except User.DoesNotExist:
        return Response({"exists": False})
