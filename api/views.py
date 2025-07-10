from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import PremiacaoSerializer, JogoLoteriaSerializer, JogoSerializer
from .models import Premiacao, JogoLoteria, Jogo

# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):

        return Response({"message": "Hello, World!"})
    

class PremiacaoViewSet(ModelViewSet):
    queryset = Premiacao.objects.all()
    serializer_class = PremiacaoSerializer


class JogoLoteriaViewSet(ModelViewSet):
    queryset = JogoLoteria.objects.all()
    serializer_class = JogoLoteriaSerializer


class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    
