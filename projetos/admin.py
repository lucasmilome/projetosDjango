from django.contrib import admin
from projetos.models import Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'tecnologia', 'publicado')
    list_filter = ('tecnologia',)
    ordering = ('tecnologia',)
    search_fields = ('titulo',)
    

