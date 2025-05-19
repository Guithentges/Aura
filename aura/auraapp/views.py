from django.shortcuts import render
from .models import Produto, Categoria

# Create your views here.
def index(request):

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'auraapp/index.html', {'produtos':produtos, 'categorias':categorias})