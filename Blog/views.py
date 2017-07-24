from django.views import generic

from . import models

class IndexView(generic.ListView):
    model = models.Article
    context_object_name = "articles"
    template_name = "Blog/index.html"


class ArticleListView(generic.ListView):
    template_name = "Blog/article_list.html"
    model = models.Article
    context_object_name = "articles"

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
