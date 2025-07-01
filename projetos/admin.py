from django.contrib import admin
from projetos.models import Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo_alias', 'descricao_alias', 'tecnologia_alias')
    list_filter = ('tecnologia',)
    ordering = ('tecnologia',)
    search_fields = ('titulo',)

    @admin.display(description='Título')
    def titulo_alias(self, obj):
        return obj.titulo
    
    @admin.display(description='Descrição')
    def descricao_alias(self,obj):
        return obj.descricao
    
    @admin.display(description='Tecnologia')
    def tecnologia_alias(self,obj):
        return obj.tecnologia