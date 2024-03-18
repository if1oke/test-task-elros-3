from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserRegistrationView, UserProfileView, UserLoginView

urlpatterns = [
    path('', UserProfileView.as_view(), name='user-profile'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegistrationView.as_view(), name='user-create'),
    path('token/', TokenRefreshView().as_view(), name='user-token')
]
