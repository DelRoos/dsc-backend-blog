from rest_framework.serializers import (
        SerializerMethodField,
        HyperlinkedRelatedField
    )
from rest_framework import serializers 
from .models import Evenement
from rest_framework.reverse import reverse
from django.http import HttpRequest

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = (
                    'speaker',
                    'title',
                    'banner',
                    'date_event', 
                    'date_pub',
                    'chapter_url',
                )

class EventCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Evenement
        fields = (
                    'speaker',
                    'title',
                    'banner',
                    'date_event', 
                    'date_pub',
                    'chapter_url',
                )

