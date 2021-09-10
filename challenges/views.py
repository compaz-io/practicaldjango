from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("<body>Eat no meat for the entire month!</body>")

def february(request):
    return HttpResponse("<body>Walk for at least 20 minutes every day!</body>")