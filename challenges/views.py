from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    'january': '<body>Eat no meat for the entire month!</body>',
    'february': '<body>Walk for at least 20 minutes every day!</body>',
    'march': '<body>Learn Django for at least 20 minutes every day!</body>',
    'april': '<body>Learn Django for at least 20 minutes every day!</body>',
    'may': '<body>Learn Django for at least 20 minutes every day - may!</body>',
    'june': '<body>Learn Django for at least 20 minutes every day! - june</body>',
    'july': '<body>Learn Django for at least 20 minutes every day! - july</body>',
    'august': '<body>Learn Django for at least 20 minutes every day! - august</body>',
    'september': '<body>Learn Django for at least 20 minutes every day! - sep</body>',
    'october': '<body>Learn Django for at least 20 minutes every day! oct</body>',
    'november': '<body>Learn Django for at least 20 minutes every day! nov</body>',
    'december': '<body>Learn Django for at least 20 minutes every day! dec</body>',
}

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Month is not supported")

    return HttpResponse(challenge_text)