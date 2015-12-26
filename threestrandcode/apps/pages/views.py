from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def apply(request):
    return render(request, "pages/apply.html")


def init(request):
    return JsonResponse({
        "csrf_token": get_token(request)
    })
