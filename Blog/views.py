from django.views import generic

from . import models

class IndexView(generic.ListView):
    model = models.Article
    context_object_name = "articles"
    template_name = "Blog/index.html"


class ArticleDetailView(generic.DetailView):
    model = models.Article
    slug_url_kwarg = "slug"
    template_name = "Blog/article.html"


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
        context["articles"] = models.Article.objects.filter(topic=self.obj)
        return context

# def view_topics(request):
#     topics = Topic.objects.all()
#     return render(request, "Blog/topics.html", {"topics": topics})

# def topic(request, user_topic):
#     print(user_topic)
#     user_topic = user_topic.title()
#     articles = Article.objects.filter(topic__name=user_topic)

#     if not articles:
#         articles = []
#     return render(request, "Blog/topic.html", {"articles": articles, "topic": user_topic})
# def index(request):
#     Articles = Article.objects.all()

#     if not Articles:
#         Articles = {}
#     return render(request, "Blog/index.html", {"Articles": Articles})

# def view_Article(request, Article_slug):
#     print(Article_slug)
#     try:
#         Article = Article.objects.get(slug=Article_slug)
#         print(Article)
#     except Article.DoesNotExist:
#         raise Http404

#     return render(request, "Blog/Article.html", {"Article": Article})

