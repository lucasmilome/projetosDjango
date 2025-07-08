from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(verbose_name='Nome Categoria', max_length=60)
   
    def __str__(self):
        return self.nome

class Postagem(models.Model):
    titulo = models.CharField(verbose_name='Título',max_length=255)
    corpo = models.TextField(verbose_name='Mensagem')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    ultima_modificacao = models.DateTimeField(verbose_name='Última modificação', auto_now=True)
    categorias = models.ManyToManyField('Categoria', related_name='postagens')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.CharField(verbose_name='Autor', max_length=60)
    corpo = models.TextField(verbose_name='Mensagem')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.autor} em {self.postagem}'