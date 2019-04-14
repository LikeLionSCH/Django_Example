from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def index(request):
    now = timezone.localtime()

    check = (now.hour >= 12)

    weekday = {
        0: "월",
        1: "화",
        2: "수",
        3: "목",
        4: "금",
        5: "토",
        6: "일",
    }

    return render(request, "index.html", {
        "now": now,
        "weekday": weekday[now.weekday()],
        "hour": now.hour % 12,
        "check": check,
    })
