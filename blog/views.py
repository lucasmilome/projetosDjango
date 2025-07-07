from django.shortcuts import render
from blog.models import Postagem, Comentario

# Create your views here.
def blog_index(request):
    postagens = Postagem.objects.all().order_by('-criado_em')

    context = {
        'postagens': postagens, 
    }

    return render(request, 'blog/blog_index.html', context)

def blog_categoria(request, categoria):
    postagens = Postagem.objects.filter(
        categorias_name_contains=categoria
    ).order_by('-criado_em')

    context = {
        'categoria': categoria,
        'postagens': postagens,
    }
    
    return render(request, 'blog/blog_categoria.html', context)

def blog_detalhe(request, pk):
    postagem = Postagem.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(postagem=postagem)

    context = {
        'postagem': postagem,
        'comentarios': comentarios,
    }

    return render(request, 'blog/blog_detalhe.html', context)