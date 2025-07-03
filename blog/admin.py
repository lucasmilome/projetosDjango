from django.contrib import admin
from blog.models import Postagem, Comentario, Categoria

# Register your models here.
@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
   pass

   
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
   pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
   pass