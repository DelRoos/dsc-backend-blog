from django.urls import path
from .views import (
    EventListView,

    EventCreateView,
)

app_name = "evenements"
urlpatterns = [
    path('evenements/', EventListView.as_view(), name="list_all_event"),
    path('evenements/create/', EventCreateView.as_view(), name="create_event"),
]