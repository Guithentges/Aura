from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, default='Descrição')
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
    imagem = models.ImageField(upload_to='./static/', default='./static/blazer.png')
    emAlta = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    tamanho = models.CharField(max_length=5, default='M')
    finalizado = models.BooleanField(default=False)  

    def subtotal(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade}"
