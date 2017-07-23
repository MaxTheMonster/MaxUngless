from django.contrib import admin
from Blog import models

# Register your models here.

admin.site.register(models.Article)
admin.site.register(models.Topic)
