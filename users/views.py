import secrets
import string
from random import random

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, FormView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm, PasswordResetForm, UserProfileForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    # template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False  # set user as inactive
        token = secrets.token_hex(16)  # generate token
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'

        send_mail(subject='Подтвердите свой адрес электронной почты',
                  message=f'Пожалуйста, подтвердите свой адрес электронной почты, нажав на ссылку: {url}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email]
                  )

        return super().form_valid(form)


def email_verify(request, token):
    # user = User.objects.get(email_confirmation_token=token)
    user = get_object_or_404(User, token=token)
    user.is_active = True
    # user.email_confirmation_token = None
    user.save()
    return redirect(reverse('users:login'))


# User = get_user_model()


class PasswordResetForm(FormView):
    template_name = 'password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()  # Используйте вашу модель
        if user:
            new_password = get_random_string(8)  # Генерация нового пароля
            user.password = make_password(new_password)
            user.save()
            # Отправка письма с новым паролем
            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('users:login')