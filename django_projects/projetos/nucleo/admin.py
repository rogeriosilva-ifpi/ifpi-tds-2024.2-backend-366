from django.contrib import admin
from nucleo.models import Projeto, Equipe, Membro, Tarefa


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'equipe', 'data_inicio', 'data_fim', 'orcamento')
    search_fields = ('nome', 'descricao')
    list_filter = ('equipe',)
    date_hierarchy = 'data_inicio'


class MembroInline(admin.TabularInline):
    model = Membro
    extra = 0


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total_membros','ativa')
    list_filter = ('ativa',)

    inlines = [MembroInline]


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'nome', 'membro', 'data_inicio', 'data_fim')
    list_filter = ('projeto', 'membro')