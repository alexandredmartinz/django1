from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto, Cliente
from django.http import HttpResponse
from django.template import loader

# A função loaders.get_template() retorna um objeto Template do tipo django.template.Template.
# Para cada requisição recebida(request), renderiza a requisição e o template index.html
# render é uma função que recebe a requisição, o template e o contexto.
# O contexto é um dicionário que será passado para o template index.html
# O template é o arquivo html que será renderizado.
# O render retorna uma resposta para o navegador.
# O render recebe a requisição, o template e o contexto.
# Utilizando o comando sheel e digitar dir(Produto) para ver os atributos do objeto Produto.
# comando dir(Produto) retorna os atributos do objeto Produto.
# comando produto.pk retorna o id do objeto Produto.
# comando produto.nome retorna o nome do objeto Produto.
# comando produto.preco retorna o preço do objeto Produto.
# comando produto.estoque retorna o estoque do objeto Produto.
# comando save() salva o objeto Produto no banco de dados.
# Para instanciar um objeto no shell, utilizar o comando Produto().   
# context é um dicionário que será passado para o template index.html


# Importar de .models import Produto 

# produto = Produto.objects.all() retorna todos os produtos do banco de dados.

#A view produto recebe um parâmetro chamado pk, que é o id do produto.
# O id do produto é o mesmo que o id do objeto Produto.
# O id do objeto Produto é o mesmo que o id do banco de dados.  
# O id do banco de dados é o mesmo que o id do objeto Produto.
# Na página produto.html, o id do produto é passado como parâmetro para a view produto.
# produto = Produto.objects.get(pk=pk) retorna o produto com o id pk.

# O parâmetro pk é o id do produto.
#Criar uma res



def index(request):
    produtos = Produto.objects.all()

    context = { 
        'title': 'Estudos Django',
        'year': '2022',
        'message': 'Seja bem vindo, estudar é muito bom!', 
        'produtos': produtos,
    }
    return render(request, 'index.html', context)

# a função index recebe um parâmetro chamado request.
# O parâmetro request é uma requisição HTTP.
# Requisições recebidas pelo servidor são armazenadas em uma variável request.
# Para cada requisisição recebida(request), renderiza a requisição e o template contato.html
# render é uma função que recebe a requisição, o template e o contexto.
# O contexto é um dicionário que será passado para o template contato.html
# O template é o arquivo html que será renderizado.
# O render retorna uma resposta para o navegador.


def contato(request):
    clientes = Cliente.objects.all()

    context = {
        'contato': 'AlexDev',
        'email': 'alexdev@dev.com',
        'clientes': clientes,
    }
    return render(request, 'contato.html', context)

# As chaves contato, email e clientes são os nomes dos atributos do contexto e no template contato.html é onde os atributos são utilizados.
# O conteúdo das chaves contato, email e clientes são os valores dos atributos do contexto.
# clientes = Cliente.objects.all() retorna todos os clientes do banco de dados.



def produto(request, pk):
    #prod = Produto.objects.get(pk=pk)
    prod = get_object_or_404(Produto, pk=pk)

    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)

# pk=pk trará o elemento produto com o id pk e armazene em prod.
# pk=pk é o parâmetro que é passado para a view produto.
# A chave 'produto' dentro de context é o nome do atributo do objeto Produto e em produto.html é onde o atributo é chamado.
# produto = Produto.objects.get(pk=pk) retorna o produto com o id pk.
# produto.pk retorna o id do objeto Produto.
# Para cada requisição recebida(request), renderiza a requisição e o template produto.html
# render é uma função que recebe a requisição, o template e o contexto.
# O contexto é um dicionário que será passado para o template produto.html
# O template é o arquivo html que será renderizado.
# O render retorna uma resposta para o navegador.
# A função get_object_or_404() retorna um objeto do tipo Produto, ou retorna um erro 404.
# Traz um objeto do tipo Produto com o id pk, caso não encontre um objeto com o id pk, retorna um erro 404.

def error404(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html', status=404)

# A função error404 recebe um parâmetro chamado request e utiliza o parâmetro exception para retornar um erro 404.
# O parâmetro exception é o erro que o servidor retorna.
# O erro 404 é o código de status HTTP que indica que a página não foi encontrada.
#A variavel template utiliza o loader para carregar o template error404.html.

def error500(request):
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html', status=500)