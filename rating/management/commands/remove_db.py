from django.core.management.base import BaseCommand
from rating.models import Rating

class Command(BaseCommand):
    help = 'remove added entries from rating model'

    def handle(self, *args, **options):
        Rating.objects.filter(text='Created from command line').delete()
