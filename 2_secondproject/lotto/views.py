from django.shortcuts import render
import random

# Create your views here.

def home(request):
    lotto = []
    random_num = random.randint(1, 46)

    for i in range(7):
        while random_num in lotto:
            random_num = random.randint(1, 46)

        lotto.append(random_num)

    return render(request, "home.html", {
        "first": lotto[0],
        "second": lotto[1],
        "third": lotto[2],
        "fourth": lotto[3],
        "fifth": lotto[4],
        "sixth": lotto[5],
        "bonus": lotto[6],
        "lotto": lotto,
    })
