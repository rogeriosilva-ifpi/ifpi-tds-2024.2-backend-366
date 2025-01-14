from django.contrib import admin
from core.models import Montadora


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
  list_display = ('nome', 'pais', 'ano_fundacao')
  search_fields = ('nome', 'pais')
  list_filter = ('pais', )

# TODO: Modelo Veiculos

# admin.site.register(Montadora, MontadoraAdmin)
