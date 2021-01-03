from rest_framework.generics import (ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,)
from .models import UserProfile
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer, ProfileDetailSerializer, UserListPostSerializer

# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileDetailSerializer

class PostUserListView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListPostSerializer
