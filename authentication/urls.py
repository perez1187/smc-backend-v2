from django.urls import path
from .views import RegisterView, UserAPIVIew, MeAPIView,LogoutAPIView, ChangePasswordView, LoginAPIView, VerifyEmail ,LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView, ResendEmailActivationView
from rest_framework_simplejwt.views import (
        TokenRefreshView,
)

#auth/
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('user/<int:id>', UserAPIVIew.as_view(), name="me"),
    path('me', MeAPIView.as_view(), name="me"),
    path('password', ChangePasswordView.as_view(), name="password"),
    path('login/', LoginAPIView.as_view(), name="login"),
    
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('resend-activation-email/', ResendEmailActivationView.as_view(), name="resend-activation-email"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
          name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
          PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),
          name='password-reset-complete')
]
