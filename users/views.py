import secrets

from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm
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


        # form.instance.is_active = False
        return super().form_valid(form)

def email_verify(request, token):
    # user = User.objects.get(email_confirmation_token=token)
    user = get_object_or_404(User, token=token)
    user.is_active = True
    # user.email_confirmation_token = None
    user.save()
    return redirect(reverse('users:login'))

