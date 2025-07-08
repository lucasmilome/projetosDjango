from django.contrib import admin
from blog.models import Postagem, Comentario, Categoria

# Register your models here.
@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
   list_display = ('titulo', 'criado_em', 'ultima_modificacao')

   
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
   pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
   pass