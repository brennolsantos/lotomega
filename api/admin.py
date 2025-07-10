from django.contrib import admin
from .models import Premiacao, JogoLoteria, Jogo
# Register your models here.

class PremiacaoAdmin(admin.ModelAdmin):
    pass

class JogoLoteriaAdmin(admin.ModelAdmin):
    filter_horizontal = ('premiacoes',)

class JogoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Premiacao, PremiacaoAdmin)
admin.site.register(JogoLoteria, JogoLoteriaAdmin)
admin.site.register(Jogo, JogoAdmin)
