from django.shortcuts import render
from .models import Event_manager
from utils.pagination import EventPageNumberPagination
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView
)
from .serializers import (  
    EventListSerializer
)

class EventListView(ListAPIView):
    queryset = Event_manager.objects.all()
    serializer_class = EventListSerializer
    pagination_class = EventPageNumberPagination
