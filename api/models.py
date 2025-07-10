from django.db import models

class Premiacao (models.Model):
    
    numeros = models.IntegerField(null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    fixo = models.BooleanField(default=False, null=False, blank=False)
    percentual = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Premiação'
        verbose_name_plural = 'Premiações'
        ordering = ['valor']

    def __str__(self):
        jogo = JogoLoteria.objects.filter(premiacoes=self).first()
        return f"Premiação {jogo.nome} - {self.numeros} números: {self.valor} {'(Fixo)' if self.fixo else ''} {'(Percentual)' if self.percentual else ''}"

# Create your models here.
class JogoLoteria(models.Model):
    
    nome = models.CharField(max_length=100, blank=False, null=False)
    max_numeros = models.IntegerField(null=False, blank=False)
    numeros_sorteados = models.IntegerField(null=False, blank=False)
    qtd_sorteios = models.IntegerField(null=False, blank=False)
    premiacoes = models.ManyToManyField(Premiacao, related_name='jogos', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    premio_bruto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Jogo Loteria'
        verbose_name_plural = 'Jogos Loteria'
        ordering = ['-data_criacao']


class Jogo(models.Model):
    jogo_loteria = models.ForeignKey(JogoLoteria, on_delete=models.CASCADE, related_name='jogos')
    numeros = models.CharField(max_length=100, blank=False, null=False)
    data_jogo = models.DateTimeField(auto_now_add=True)
    premiado = models.BooleanField(default=False, null=False, blank=False)
    valor_premio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.jogo_loteria.nome} - {self.numeros}"
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['-data_jogo']
