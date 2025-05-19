from django.contrib import admin
from auraapp.models import Produto, Categoria, Cliente, Pedido


#login admin
#senha admin

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Pedido)
