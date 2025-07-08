from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=180)
    descricao = models.TextField(verbose_name='Descrição')
    tecnologia = models.CharField(verbose_name='Tecnologia', max_length=20)
    imagem = models.FileField(verbose_name='Imagem',upload_to='imagens_projetos', blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo.title()