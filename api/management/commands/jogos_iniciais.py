from django.core.management.base import BaseCommand
from api.models import JogoLoteria, Premiacao

class Command(BaseCommand):
    help = "Cria os jogos principais da loteria"

    def handle(self, *args, **options):
        pass
