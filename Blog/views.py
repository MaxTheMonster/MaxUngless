from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "Blog/index.html", {"posts": posts})

def view_post(request, post_slug):
    print(post_slug)
    try:
        post = Post.objects.get(slug=post_slug)
        print(post)
    except Post.DoesNotExist:
        raise Http404

    return render(request, "Blog/post.html", {"post": post})

def work(request):
    return render(request, "Blog/work.html")
