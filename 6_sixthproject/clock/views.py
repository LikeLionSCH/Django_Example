from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def fill_zero(num):
    if num < 10:
        return "0" + str(num)

    return num


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

    month = fill_zero(now.month)
    day = fill_zero(now.day)
    hour = fill_zero(now.hour)
    minute = fill_zero(now.minute)
    second = fill_zero(now.second)

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
