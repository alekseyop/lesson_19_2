from django.contrib.auth.forms import UserCreationForm



# from users.forms import StyleFormMixin
from users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
