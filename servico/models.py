from django.db import models

class Servico (models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField(max_length = 200)
    imagem = models.ImageField( upload_to='produto_imagens/%Y/%m/', blank = True, null = True)
    slug = models.SlugField(unique = True)
    preco = models.FloatField(default = 0)
    tipo = models.CharField(
        default = 'V',
        max_length=1,
        choices = (
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )