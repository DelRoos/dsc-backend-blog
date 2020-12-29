from django.urls import path
from .views import (
    EventListView
)

app_name = "events"
urlpatterns = [
    path('', EventListView.as_view(), name="list_all_event")
]