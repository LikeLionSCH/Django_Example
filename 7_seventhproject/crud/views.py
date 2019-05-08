from django.shortcuts import render, redirect, get_object_or_404
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
    post.created_at = timezone.now()
    post.updated_at = timezone.now()

    post.save()

    return redirect("index")


def read(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, "read.html", {
        "post": post,
    })



def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.title = request.GET["title"]
    post.body = request.GET["body"]
    post.updated_at = timezone.now()

    post.save()

    return redirect("index")


def update_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, "update.html", {
        "post": post,
    })


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    return redirect("index")
