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
# git init significa que o projeto será armazenado no git.
# git add . significa que o projeto será adicionado ao git.
# git commit -m "mensagem" significa que o projeto será commitado com a mensagem "mensagem".
# git config --global user.email " significa que o email do usuário será configurado.
# git config --global user.name " significa que o nome do usuário será configurado.


# Procfile é um arquivo que é utilizado para definir qual o servidor web que será utilizado.
# O comando web: gunicorn django1.wsgi --log-file - significa que o gunicorn irá rodar o django1.wsgi.
# O heroku é um servidor web que permite que o Django o servidor web seja configurado automaticamente.
# heroku login é para logar no heroku.
# No terminal usar ocomando heroku login para logar no heroku.
# Criar uma aplicação no heroku com o comando heroku create, utilizar o nome do projeto.
# o comando --buildpack heroku/python significa que o heroku irá configurar o projeto como um buildpack do heroku.
# O comando heroku open irá abrir o projeto no navegador.
# heroku create serve para criar uma aplicação no heroku.

# executar o comando git push heroku master clicar enter  para enviar o projeto para o heroku.
# git push heroku master vai enviar o projeto para o heroku. 
# web: gunicorn django1.wsgi --log-file - significa que o gunicorn irá rodar o django1.wsgi.

