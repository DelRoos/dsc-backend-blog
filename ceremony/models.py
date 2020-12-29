from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Ceremony(models.Model):
    user = models.ForeignKey(User ,related_name="ceremonies", on_delete=models.CASCADE)
    titre = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)
    speaker = models.CharField(max_length=200, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=False)
    banner = models.URLField(max_length=1000, blank=True)
    article_link = models.URLField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ceremony_day = models.DateTimeField(blank=True)


    def save(self, *args, **kwargs):
        value = self.titre
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
