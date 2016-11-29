from django.shortcuts import render
from .models import Post, Topic
from django.http import Http404


def index(request):
    posts = Post.objects.all()

    if not posts:
        posts = {}
    return render(request, "Blog/index.html", {"posts": posts})

def view_post(request, post_slug):
    print(post_slug)
    try:
        post = Post.objects.get(slug=post_slug)
        print(post)
    except Post.DoesNotExist:
        raise Http404

    return render(request, "Blog/post.html", {"post": post})

def view_topics(request):
    topics = Topic.objects.all()
    return render(request, "Blog/topics.html", {"topics": topics})

def topic(request, user_topic):
    print(user_topic)
    user_topic = user_topic.title()
    articles = Post.objects.filter(topic__name=user_topic)

    if not articles:
        articles = []
    return render(request, "Blog/topic.html", {"articles": articles, "topic": user_topic})
