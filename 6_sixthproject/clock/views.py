from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def index(request):
    now = timezone.localtime()

    return render(request, "index.html", {
        "weekday": now.weekday(),
        "month": now.month,
        "day": now.day,
        "hour": now.hour % 12,
        "minute": now.minute,
        "second": now.second,
        "check": now.hour >= 12,
    })
