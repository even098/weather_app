from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration_api'),  # для регистрации пользователя
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # для получения токенов (access/refresh)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # для обновления токенов через refresh
]
