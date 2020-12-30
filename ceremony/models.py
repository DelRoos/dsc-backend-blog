from django.db import models
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    speaker = models.CharField(max_length=255)
    title = models.CharField(max_length=200, blank=False, unique=True)
    banner = models.URLField(max_length=500, blank=True)
    date_event = models.DateTimeField(auto_now_add=True)
    date_pub = models.DateTimeField(auto_now=True)
    chapter_url = models.URLField(max_length=500, blank=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)