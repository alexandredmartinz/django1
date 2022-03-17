# Usar o shell do python utilizar manage.py sheel e digitar  from core.models import Cliente e Cliente.objects.all() para ver todos os clientes.
# Para alterar o nome do cliente, utilizar o comando Cliente.nom = 'Novo nome' e Cliente.save() para salvar o novo nome.
# Para deletar o cliente, utilizar o comando Cliente.delete() para deletar o cliente.
# Para criar um novo cliente, utilizar o comando Cliente.objects.create(nome='Novo nome', sobrenome='Novo sobrenome',
# Para verificar o nome de todos dos clientes, utilizar o comando Cliente.objects.all()
#  WSGI é um protocolo de aplicação web que permite ao servidor web executar uma aplicação Python.

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

# O static serve para servir arquivos estáticos, como imagens, css, js, etc.
#/static/ está sendo utilizado para servir os arquivos estáticos.
# Em settings.py, cria a variavel STATIC_ROOT para definir o diretório onde os arquivos estáticos serão salvos.
# O comando STATIC_ROOT é um atributo de settings.py.
# Dentro de core criar pasta static e dentro de static criar pastas css e js.
# 'staticfiles' será usado em produção para servir os arquivos estáticos.


#Para qualquer template que for utilizar o css ou js, utilizar o comando {% load static %}
# Para utilizar o css ou js, informar dentro do template e no <head>  {% static 'css/stilos.css' %}.
# No template index.html, utilizar link <link rel="stylesheet" href="{% static 'css/stilos.css' %}">
# para carregar imagens no template, utilizar {% static 'imagens/imagem.png' %}
# Para carregar js no template, utilizar {% static 'js/script.js' %}

# Colocar em produção, utilizar o comando collectstatic para copiar os arquivos estáticos para o diretório STATIC_ROOT.
#whitneoise feito para mostrar os arquivos estáticos.


# O collectstatic é utilizado para copiar os arquivos estáticos para o diretório definido em STATIC_ROOT.
# O comando collectstatic é executado pelo comando manage.py.

# Por padrão o Django o servidor não consegue servir arquivos estáticos.
# Para permitir que o Django o servidor consegue servir arquivos estáticos, quando está no modo de produção.

# gunicorn é para rodar o servidor web.
# whitnoise é para mostrar os arquivos estáticos.


# whitenoise.middleware.WhiteNoiseMiddleware significa que o Django irá usar o WhiteNoise para compartilhar arquivos estáticos entre servidores. 

# importante criar o arquivo gitignore para ignorar determinados arquivos, exemplo: __pycache__, static, media, etc.