from django.views import generic

from . import models

class IndexView(generic.ListView):
    model = models.Post
    template_name = "Blog/index.html"


class PostDetailView(generic.DetailView):
    model = models.Post
    slug_url_kwarg = "slug"
    template_name = "Blog/post.html"


class TopicListView(generic.ListView):
    model = models.Topic
    template_name = "Blog/topics.html"


class TopicDetailView(generic.DetailView):
    template_name = "Blog/topic.html"

    def get_queryset(self):
        self.obj = models.Topic.objects.filter(slug=self.kwargs["slug"])
        return self.obj

    def get_context_data(self, *args, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context["articles"] = models.Post.objects.filter(topic=self.obj)
        return context

# def view_topics(request):
#     topics = Topic.objects.all()
#     return render(request, "Blog/topics.html", {"topics": topics})

# def topic(request, user_topic):
#     print(user_topic)
#     user_topic = user_topic.title()
#     articles = Post.objects.filter(topic__name=user_topic)

#     if not articles:
#         articles = []
#     return render(request, "Blog/topic.html", {"articles": articles, "topic": user_topic})
# def index(request):
#     posts = Post.objects.all()

#     if not posts:
#         posts = {}
#     return render(request, "Blog/index.html", {"posts": posts})

# def view_post(request, post_slug):
#     print(post_slug)
#     try:
#         post = Post.objects.get(slug=post_slug)
#         print(post)
#     except Post.DoesNotExist:
#         raise Http404

#     return render(request, "Blog/post.html", {"post": post})

