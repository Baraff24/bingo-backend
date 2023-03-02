from bingo.models import Ball
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Command that adds balls from 1 to 90 to the database
    You have to run this command in the shell: python manage.py addBalls
    """

    help = 'Add balls to the database'

    def handle(self, *args, **options):
        if Ball.objects.all().exists():
            print('Balls already added')
            return None
        else:
            for number in range(1, 91):
                Ball.objects.create(number=number)
            print('Balls added')

            self.stdout.write(self.style.SUCCESS('Successfully added balls to the database'))
