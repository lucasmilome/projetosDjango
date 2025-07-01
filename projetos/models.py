from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=180)
    descricao = models.TextField()
    tecnologia = models.CharField(max_length=20)
    imagem = models.FileField(upload_to='imagens_projetos', blank=True)

    def __str__(self):
        return self.titulo.title()