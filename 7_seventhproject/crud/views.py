from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html", {

    })


def new(request):
    return render(request, "new.html", {
        
    })


def create(request):
    return redirect("index")
