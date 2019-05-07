from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all

    return render(request, "index.html", {
        "posts": posts,
    })


def new(request):
    return render(request, "new.html", {

    })


def create(request):
    post = Post()

    post.title = request.GET["title"]
    post.body = request.GET["body"]
    post.time = timezone.now()

    post.save()

    return redirect("index")


def read(request):
    pass


def update(request):
    pass


def delete(request):
    pass
