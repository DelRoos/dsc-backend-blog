from django.db import models

# Create your models here.
class Event(models.Model):
    speaker = models.CharField(max_length=255)
    title = models.CharField(max_length=200, blank=False, unique=True)
    banner = models.URLField(max_length=500, blank=True)
    date_event = models.DateTimeField(auto_now=False)
    date_pub = models.DateTimeField(auto_now=True)
    chapter_url = models.URLField(max_length=500, blank=True)