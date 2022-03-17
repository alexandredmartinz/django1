from django.contrib import admin

from .models import Produto, Cliente


# Django fornece um model admin para cada modelo.
# O model admin é um objeto que permite ao administrador do Django acessar e editar os modelos.
# O model admin é um objeto que herda de admin.ModelAdmin.
# Criar um super usuário admin, com o comando createsuperuser.
# Para criar um super usuário admin, precisamos informar o nome do usuário e a senha.
# inserir as classes Produto e Cliente no admin. utilizar o comando admin.site.register e inserir as classes na frente do register.
# é preciso registrar os modelos para que o Django possa acessá-los. Importa de .models

# Parar mostrar o nome, preço e estoque do produto no admin é preciso informar a class ProdutoAdmin no admin.site.register.





class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    list_filter = ('nome', 'preco', 'estoque')
    search_fields = ('nome', 'preco', 'estoque')
    ordering = ('nome', 'preco', 'estoque')

admin.site.register(Produto, ProdutoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    list_filter = ('nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome', 'email')
    ordering = ('nome', 'sobrenome', 'email')

admin.site.register(Cliente, ClienteAdmin)

