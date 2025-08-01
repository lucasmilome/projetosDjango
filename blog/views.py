from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Postagem, Comentario
from blog.forms import ComentarioForm

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

    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario(
                autor = form.cleaned_data['autor'],
                corpo = form.cleaned_data['corpo'],
                postagem = postagem,
            )
            comentario.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        'postagem': postagem,
        'comentarios': comentarios,
        'form': ComentarioForm,
    }

    return render(request, 'blog/blog_detalhe.html', context)