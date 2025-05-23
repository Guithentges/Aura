from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('/product/<produto_id>', views.product, name='produto'),
    #path('/category/<categoria_id>', views.category, name='categoria')
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/aumentar/<int:pedido_id>/', views.aumentar_quantidade, name='aumentar_quantidade'),
    path('carrinho/diminuir/<int:pedido_id>/', views.diminuir_quantidade, name='diminuir_quantidade'),
    path('carrinho/remover/<int:pedido_id>/', views.remover_item, name='remover_item'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.register_view, name='registrar'),
]