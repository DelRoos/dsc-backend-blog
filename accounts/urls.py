from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserProfileListCreateView, UserProfileDetailView, PostUserListView

urlpatterns = [
    path('rest_auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/all-profiles/',UserProfileListCreateView.as_view(),name="all-profiles"),
    path("auth/profile/<int:pk>/",UserProfileDetailView.as_view(),name="profile"),
    path("post/<int:pk>/",PostUserListView.as_view(),name="post_user"),
    
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
    path('api/token/verify/', verify_jwt_token, name='token_verify'),
    
]
