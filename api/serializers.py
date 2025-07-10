from rest_framework import serializers 
from .models import Premiacao, JogoLoteria, Jogo

class PremiacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premiacao
        fields = '__all__'

class JogoLoteriaSerializer(serializers.ModelSerializer):
    premiacoes = PremiacaoSerializer(many=True, read_only=True)

    class Meta:
        model = JogoLoteria
        fields = '__all__'
        read_only_fields = ('data_criacao', 'data_atualizacao')


class JogoSerializer(serializers.ModelSerializer):
    jogo_loteria = JogoLoteriaSerializer(read_only=True)

    class Meta:
        model = Jogo
        fields = '__all__'
        read_only_fields = ('data_jogo',)