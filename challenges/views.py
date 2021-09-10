from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "<body>Eat no meat for the entire month!</body>"
    elif month == 'february':
        challenge_text ="<body>Walk for at least 20 minutes every day!</body>"
    elif month == 'march':
        challenge_text = "<body>Learn Django for at least 20 minutes every day!</body>"
    else:
        return HttpResponseNotFound("<body>This month is not supported!</body>")

    return HttpResponse(challenge_text)