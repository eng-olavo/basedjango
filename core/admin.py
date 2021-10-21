from django.contrib import admin

from .models import Acucares, Nacionalidades, Tipos, Uvas, UvasVinhos, Vinhos


@admin.register(Acucares)
class AcucaresAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Nacionalidades)
class NacionalidadesAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Tipos)
class TiposAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Uvas)
class UvasAdmin(admin.ModelAdmin):
    list_display = ('nome',)


#
# @admin.register(UvasVinhos)
# class UvasAdmin(admin.ModelAdmin):
#     list_display = ('percentual',)



@admin.register(Vinhos)
class VinhosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'safra', 'vinicola', 'alcool', 'temperatura', 'volume', 'guarda', 'amadurecimento',
                    'visual', 'olfativo', 'gustativo', 'destaque', 'promocao', 'avaliacao', 'numero_avaliacoes',
                    'maior_avaliacao', 'ativo', 'data_criacao', 'data_atualizacao', 'id_tipo', 'id_acucar',
                    'id_uvas', 'id_nacionalidade' )

