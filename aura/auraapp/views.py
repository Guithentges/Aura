from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Pedido, Cliente
from .forms import ClienteForm

def home(request):

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    pedidos = Categoria.objects.all()
    clientes = Cliente.objects.all()

    return render(request, 'auraapp/index.html', {'produtos':produtos, 'categorias':categorias, 'pedidos':pedidos, 'clientes':clientes})

def adicionar_ao_carrinho(request, produto_id):
    cliente_id = request.session.get('cliente_id')  # Pegando cliente logado
    if not cliente_id:
        return redirect('login')  # ou sua view de login
    
    cliente = get_object_or_404(Cliente, id=cliente_id)
    produto = get_object_or_404(Produto, id=produto_id)

    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, produto=produto, finalizado=False)

    if not criado:
        pedido.quantidade += 1
    pedido.save()
    return redirect('ver_carrinho')

def ver_carrinho(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login')

    cliente = get_object_or_404(Cliente, id=cliente_id)
    itens = Pedido.objects.filter(cliente=cliente, finalizado=False)
    total = sum([item.subtotal() for item in itens])

    return render(request, 'auraapp/carrinho.html', {'itens': itens, 'total': total})

def aumentar_quantidade(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.quantidade += 1
    pedido.save()
    return redirect('ver_carrinho')

def diminuir_quantidade(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if pedido.quantidade > 1:
        pedido.quantidade -= 1
        pedido.save()
    else:
        pedido.delete()  # Se chegou a 0, remove do carrinho
    return redirect('ver_carrinho')

def remover_item(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    return redirect('ver_carrinho')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        cliente = Cliente.objects.filter(email=email, senha=senha).first()
        if cliente:
            request.session['cliente_id'] = cliente.id
            request.session['cliente_nome'] = cliente.nome
            return redirect('home')
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'auraapp/login.html')

def logout_view(request):
    # Remove todos os dados da sessão (incluindo id do cliente)
    request.session.flush()
    return redirect('home') 

def register_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = ClienteForm()
    return render(request, 'auraapp/registrar.html', {'form': form})
