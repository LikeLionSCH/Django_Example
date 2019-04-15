from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def index(request):
    now = timezone.localtime()

    weekday = {
        0: "월",
        1: "화",
        2: "수",
        3: "목",
        4: "금",
        5: "토",
        6: "일",
    }

    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    return render(request, "index.html", {
        "now": now,
        "weekday": weekday[now.weekday()],
        "month": month,
        "day": day,
        "hour": hour % 12,
        "minute": minute,
        "second": second,
        "check": now.hour >= 12,
    })
