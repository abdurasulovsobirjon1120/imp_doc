from django.urls import path
from .views import RegisterView, LoginView, ResetPasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Access va Refresh token olish uchun
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh tokenni yangilash
]