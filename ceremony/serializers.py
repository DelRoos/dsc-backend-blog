
from rest_framework import serializers 
from .models import Ceremony

class CeremonyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremony
        fields = (
                    'title',
                    'slug',
                    'speaker',
                    'description',
                    'article_link',
                    'created_at',
                    'ceremony_day'
                )