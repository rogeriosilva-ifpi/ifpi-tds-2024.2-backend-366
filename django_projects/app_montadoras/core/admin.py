from django.contrib import admin
from core.models import Montadora, ModeloVeiculo, Veiculo


class ModeloInline(admin.TabularInline):
  model = ModeloVeiculo
  extra = 0
  fields = ('nome', 'motorizacao', 'em_producao')
  show_change_link = True


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
  list_display = ('nome', 'count_veiculos', 'pais', 'ano_fundacao', 'idade')
  search_fields = ('nome', 'pais')
  list_filter = ('pais', )

  inlines = [ModeloInline]

# TODO: Modelo Veiculos
@admin.register(ModeloVeiculo)
class ModeloVeiculoAdmin(admin.ModelAdmin):
  list_display = ('nome', 'motorizacao', 'montadora')
  list_filter = ('motorizacao', 'montadora')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
  list_display = ('modelo',  'cor', 'ano', 'placa',)
  list_filter = ('modelo', )