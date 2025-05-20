from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('/product/<produto_id>', views.product, name='produto'),
    #path('/category/<categoria_id>', views.category, name='categoria')
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('login/', views.login_view, name='login'),
]