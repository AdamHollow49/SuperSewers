from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def success(request):
    return render(request, 'success.html', {})
