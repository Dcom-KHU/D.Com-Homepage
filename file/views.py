from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from file.models import FileNotice, FileActivity, FileFree, FileJokbo, FileShare, FileStudy


@csrf_exempt
@api_view(['POST'])
def notice_upload(request):
    if 'token' in request.POST and 'file' in request.FILES:
        file_obj = FileNotice.objects.create(
            token=request.POST['token'],
            file=request.FILES['file'])
        return Response({'file': file_obj.pk}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def activity_upload(request):
    if 'token' in request.POST and 'file' in request.FILES:
        file_obj = FileActivity.objects.create(
            token=request.POST['token'],
            file=request.FILES['file'])
        return Response({'file': str(file_obj.pk)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def free_upload(request):
    if 'token' in request.POST and 'file' in request.FILES:
        file_obj = FileFree.objects.create(
            token=request.POST['token'],
            file=request.FILES['file'])
        return Response({'file': str(file_obj.pk)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def jokbo_upload(request):
    if 'token' in request.POST and 'file' in request.FILES:
        file_obj = FileJokbo.objects.create(
            token=request.POST['token'],
            file=request.FILES['file'])
        return Response({'file': str(file_obj.pk)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def share_upload(request):
    if 'token' in request.POST and 'file' in request.FILES:
        file_obj = FileShare.objects.create(
            token=request.POST['token'],
            file=request.FILES['file'])
        return Response({'file': str(file_obj.pk)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def study_upload(request):
    if 'token' in request.POST and 'file' in request.FILES:
        file_obj = FileStudy.objects.create(
            token=request.POST['token'],
            file=request.FILES['file'])
        return Response({'file': str(file_obj.pk)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)




