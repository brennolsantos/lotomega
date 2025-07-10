from django.core.management.base import BaseCommand
from api.models import JogoLoteria, Premiacao

class Command(BaseCommand):
    help = "Cria os jogos principais da loteria"

    def handle(self, *args, **options):

        if JogoLoteria.objects.count() > 0:
            self.stdout.write(self.style.WARNING("Jogos já criados."))
            return

        faixa1_lotofacil = Premiacao.objects.create(
            numeros=11,
            valor=7.00,
            fixo=True,
            percentual=0
        )

        faixa2_lotofacil = Premiacao.objects.create(
            numeros=12,
            valor=14.00,
            fixo=True,
            percentual=0
        )

        faixa3_lotofacil = Premiacao.objects.create(
            numeros=13,
            valor=35.00,
            fixo=True,
            percentual=0
        )

        faixa4_lotofacil = Premiacao.objects.create(
            numeros=14,
            valor=0,
            fixo=False,
            percentual=13
        )

        faixa5_lotofacil = Premiacao.objects.create(
            numeros=15,
            valor=0,
            fixo=False,
            percentual=62
        )
        
        lotofacil  = JogoLoteria.objects.create(
            nome='Lotofácil',
            max_numeros=20,
            numeros_sorteados=15,
            qtd_sorteios=1,
            premio_bruto=43.79)

        lotofacil.premiacoes.set([
            faixa1_lotofacil,
            faixa2_lotofacil,
            faixa3_lotofacil,
            faixa4_lotofacil,
            faixa5_lotofacil
        ])

        lotofacil.save()

        faixa1_quina = Premiacao.objects.create(
            numeros=2,
            valor=0,
            fixo=False,
            percentual=10
        )

        faixa2_quina = Premiacao.objects.create(
            numeros=3,
            valor=0,
            fixo=False,
            percentual=10
        )

        faixa3_quina = Premiacao.objects.create(
            numeros=4,
            valor=0,
            fixo=False,
            percentual=15
        )

        faixa4_quina = Premiacao.objects.create(
            numeros=5,
            valor=0,
            fixo=False,
            percentual=35
        )

        quina = JogoLoteria.objects.create(
            nome='Quina',
            max_numeros=15,
            numeros_sorteados=5,
            qtd_sorteios=1,
            premio_bruto=43.79
        )

        quina.premiacoes.set([
            faixa1_quina,
            faixa2_quina,
            faixa3_quina,
            faixa4_quina
        ])

        quina.save()




        self.stdout.write(self.style.SUCCESS("Jogos iniciais criados com sucesso!"))

