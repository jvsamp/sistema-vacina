from django.contrib import admin
from .models import Paciente, Vacina, Estoque, PostoSaude

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'cpf', 'cartao_sus', 'responsavel')
    search_fields = ('nome', 'cpf', 'cartao_sus')
    list_filter = ('responsavel',)

admin.site.register(Vacina)
admin.site.register(PostoSaude)
admin.site.register(Estoque)
