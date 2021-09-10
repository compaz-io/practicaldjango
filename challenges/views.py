from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Learn Django for at least 20 minutes every day!',
    'may': 'Learn Django for at least 20 minutes every day - may!',
    'june': 'Learn Django for at least 20 minutes every day! - june',
    'july': 'Learn Django for at least 20 minutes every day! - july',
    'august': 'Learn Django for at least 20 minutes every day! - august',
    'september': 'Learn Django for at least 20 minutes every day! - sep',
    'october': 'Learn Django for at least 20 minutes every day! oct',
    'november': 'Learn Django for at least 20 minutes every day! nov',
    'december': None,
}

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    # print(list_items)
    return render(request, "challenges/index.html", {
        "months": months,

    })


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
        print(challenge_text, month.capitalize())
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month,
        })
    except:
        return HttpResponseNotFound(f"<p>Month <strong>{month}</strong> is not supported</p>")

    