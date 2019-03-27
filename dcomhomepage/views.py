from django.shortcuts import render


def index(request):
    name = '오윤석'
    return render(request, 'index.html', {'name': name})
