from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Hello World command'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Hello, World!'))