from django.db import models

# Models trabalham no padrão de herança, ou seja, cada model herda de models.Model
# Os models são os objetos que serão armazenados no banco de dados.
# Através do model, podemos criar tabelas no banco de dados.
# Através das classes o Django cria automaticamente uma tabela no banco de dados.

# A classe Produto vai herdar do módulo models a class Model, ela extende a classe Model.
# O nome da classe Produto é o nome da tabela no banco de dados.
# O nome da tabela no banco de dados é produtos.
#  Podemos criar atributos como por exemplo: nome e define o tipo de dado do atributo.

# Estou informando ao Django qu estou criando um atributo do tipo CharField, que é um tipo de dado do Django.
# Maxlength é o tamanho máximo do campo, criando um objeto do tipo produto
# integer field siginifica que o campo será do tipo inteiro.


# Para que possamos executar as migrations, precisamos informar o nome da aplicação no arquivo settings.py
# Migration é um arquivo que contém as alterações no banco de dados.
# o comando makemigrations pega todos os models da aplicação e cria um arquivo de migration.
# arquivo inicial de migration: 0001_initial.py. E pode gerenciar o histograma de alterações.
# o banco de dados é o sqlite3.
# Ao criar outro modelo será criado uma nova migration.
# Através do arquivo de migration é possível voltar atrás.

# O comando migrate executa as alterações no banco de dados.
# Ao aplicar o comando migrate, o banco de dados será atualizado.

# o medodo __Str__ é um método que retorna o nome do modelo.
# Para usar o shell importa a classe Cliente e produto de core.models e executa o comando python manage.py shell


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100) #Colocar um label para o atributo nome.
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2) #Colocar um label para o atributo preco.
    estoque = models.IntegerField('Quantidade em Estoque') #Colocar um label para o atributo estoque.

    def __str__(self):
        return self.nome #Retorna o nome do produto.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome #Retorna o nome do cliente.