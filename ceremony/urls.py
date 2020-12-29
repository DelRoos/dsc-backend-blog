from django.urls import path
from .views import CeremonyListView

urlpatterns = [
    path("events/", CeremonyListView.as_view(), name='ceremony'),
]