from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    # help = 'Create superuser'
    #
    # def add_arguments(self, parser):
    #     parser.add_argument('email', type=str)
    #     parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        # User.objects.create_superuser(
        #     options['email'],
        #     options['password'],
        # )
        user = User.objects.create(email='test5@test.com')
        user.set_password('362362')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
