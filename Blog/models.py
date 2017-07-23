from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse

class Topic(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        return super(Topic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"slug": self.slug})


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(editable=False)
    published = models.DateField(default=timezone.now)
    topic = models.ForeignKey(Topic)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
