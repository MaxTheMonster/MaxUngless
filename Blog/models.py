import datetime

from django.db import models
from django.template.defaultfilters import slugify


class Topic(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(default="slug")
    published = models.DateField(default=datetime.datetime.now())
    topic = models.ForeignKey(Topic)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
