from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__ (self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='static/product/', default='./static/blazer.png')

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.produto