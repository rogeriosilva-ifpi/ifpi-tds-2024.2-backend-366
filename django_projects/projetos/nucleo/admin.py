from django.contrib import admin
from nucleo.models import Projeto, Equipe, Membro, Tarefa

class TarefaInline(admin.TabularInline):
    model = Tarefa
    fields = ('nome', 'membro', 'horas_estimadas', 'data_inicio')
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
      if db_field.name == "membro":
        if request.resolver_match:
          projeto_id = request.resolver_match.kwargs.get('projeto_id')
          if projeto_id:
            kwargs["queryset"] = Membro.objects.filter(equipe__projeto__id=projeto_id)
      return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'equipe', 'data_inicio', 'data_fim', 'orcamento')
    search_fields = ('nome', 'descricao')
    list_filter = ('equipe',)
    date_hierarchy = 'data_inicio'

    inlines = [TarefaInline]


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