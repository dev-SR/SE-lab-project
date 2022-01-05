
# Entire place
# Private rooms
# Hotel rooms
# Shared rooms
from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates facilities"

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
    """

    def handle(self, *args, **options):
        room_types = [
            'Entire place',
            'Private rooms',
            'Hotel rooms',
            'Shared rooms',
        ]
        for f in room_types:
            RoomType.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(
            f"{len(room_types)} rooms types created!"))
