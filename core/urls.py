#Neste caso criar um arquivo urls.py para o app core, e importar o arquivo urls.py de cada app, para que o Django possa encontrar as URLs.
#Importar o path de from.views import index, contato
#Importar de from.django.urls import path
#Toda requisição para home envia para a view index
#Toda requisição para contato envia para a view contato
#Primeiro chama a url, depois a view e depois o template.




from django.urls import path
from.views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]