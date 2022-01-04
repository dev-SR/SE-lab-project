from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command tells me that the app is working"

    def add_arguments(self, parser):
        parser.add_argument(
            "--n", help="Number of times to repeat", type=int
        )

    def handle(self, *args, **options):
        print(args, options)
        times = options.get("n", 1)
        for t in range(times+1):
            self.stdout.write(self.style.SUCCESS(t))
