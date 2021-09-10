from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    print(list_items)
    return HttpResponse(list_items)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html')
    except:
        return HttpResponseNotFound(f"<p>Month <strong>{month}</strong> is not supported</p>")

    