import random
import string

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            help='Username to use for login (default: tbhaxor)',
            default='tbhaxor')
        parser.add_argument(
            "--password",
            help='Password for the admin account to use. If not passed, it will generate and print on stdout')

    def handle(self, *args, **options):
        password = options.get('password')
        username = options.get('username')

        user = User.objects.filter(username=username).first()
        if user is not None:
            raise CommandError(f'Username {username} already exists.')

        if password is None:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            self.stdout.write(self.style.SUCCESS(f'The password for {username} is {password}.'))
            self.stdout.write(self.style.SUCCESS('We recommend you to change it after first login.'))

        User.objects.create_superuser(username=username, password=password)
