from django.conf.urls import url
from django.contrib import admin
from Blog import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name="index"), 
    url(r'^topics/$', views.TopicListView.as_view(), name="topic_list"),
    url(r'^topics/(?P<slug>[-\w]+)/', views.TopicDetailView.as_view(), name="topic_detail"),
    url(r'^articles/(?P<slug>[-\w]+)/', views.ArticleDetailView.as_view(), name="article_detail"),
    url(r'^articles/$', views.ArticleListView.as_view(), name="article_list"),
    url(r'^work/', TemplateView.as_view(template_name="Blog/work.html"), name="work"),
    url(r'^contact/', TemplateView.as_view(template_name="Blog/contact.html"), name="contact"),
]
