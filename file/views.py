from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from file.models import FileNotice, FileActivity, FileFree, FileJokbo, FileShare, FileStudy


@csrf_exempt
def notice_upload(request):
    if 'dropzone-token' in request.POST and 'file' in request.FILES:
        pk_list = []
        for file in request.FILES.getlist('file'):
            file_obj = FileNotice.objects.create(
                token=request.POST['dropzone-token'],
                file=file)
            pk_list.append(file_obj.pk)
        return JsonResponse({'file': pk_list}, status=200)
    else:
        return JsonResponse({'message': 'key error'}, status=400)


@csrf_exempt
@api_view(['POST'])
def activity_upload(request):
    if 'dropzone-token' in request.POST and 'file' in request.FILES:
        pk_list = []
        for file in request.POST['file']:
            file_obj = FileActivity.objects.create(
                token=request.POST['dropzone-token'],
                file=file)
            pk_list.append(file_obj.pk)
        return Response({'file': pk_list}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def free_upload(request):
    if 'dropzone-token' in request.POST and 'file' in request.FILES:
        pk_list = []
        for file in request.POST['file']:
            file_obj = FileFree.objects.create(
                token=request.POST['dropzone-token'],
                file=file)
            pk_list.append(file_obj.pk)
        return Response({'file': pk_list}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def jokbo_upload(request):
    if 'dropzone-token' in request.POST and 'file' in request.FILES:
        pk_list = []
        for file in request.POST['file']:
            file_obj = FileJokbo.objects.create(
                token=request.POST['dropzone-token'],
                file=file)
            pk_list.append(file_obj.pk)
        return Response({'file': pk_list}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def share_upload(request):
    if 'dropzone-token' in request.POST and 'file' in request.FILES:
        pk_list = []
        for file in request.POST['file']:
            file_obj = FileShare.objects.create(
                token=request.POST['dropzone-token'],
                file=file)
            pk_list.append(file_obj.pk)
        return Response({'file': pk_list}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def study_upload(request):
    if 'dropzone-token' in request.POST and 'file' in request.FILES:
        pk_list = []
        for file in request.POST['file']:
            file_obj = FileStudy.objects.create(
                token=request.POST['dropzone-token'],
                file=file)
            pk_list.append(file_obj.pk)
        return Response({'file': pk_list}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'key error'}, status=status.HTTP_400_BAD_REQUEST)
