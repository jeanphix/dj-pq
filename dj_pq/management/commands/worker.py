from django.core.management.base import BaseCommand

from dj_pq import get_queue


class Command(BaseCommand):
    help = 'Starts new worker'

    def add_arguments(self, parser):
        parser.add_argument('queue_name', type=str)
        parser.add_argument(
            '--burst',
            action='store_true',
            default=False,
        )

    def handle(self, **options):
        name = options['queue_name']
        burst = options['burst']
        get_queue(name).work(burst)
