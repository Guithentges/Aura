from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=150)

    def __str__(self):
        return self.nome