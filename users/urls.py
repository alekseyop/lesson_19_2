from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verify, PasswordResetForm, ProfileUpdateView, CustomPasswordChangeView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verify, name='email_confirm'),
    path('password_reset/', PasswordResetForm.as_view(), name='password_reset'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
]
