from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PremiacaoViewSet, JogoLoteriaViewSet, JogoViewSet, HelloWorldView

router = DefaultRouter()
router.register(r'premiacoes', PremiacaoViewSet, basename='premiacao')
router.register(r'jogos_loteria', JogoLoteriaViewSet, basename='jogo_loteria')
router.register(r'jogos', JogoViewSet, basename='jogo')

app_name = 'api'

urlpatterns = [
        path('', include(router.urls)),
]