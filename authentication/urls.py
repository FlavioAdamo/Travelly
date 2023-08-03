from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
   
   path('register/', UserRegisterView.as_view(), name='register'),

   path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]