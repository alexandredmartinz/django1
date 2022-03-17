"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Recomenda-se que o nome do arquivo seja o nome do app, criar um arquivo urls.py para cada app, e importar o arquivo urls.py de cada app, para que o Django possa encontrar as URLs.
# Importar o include() para que o Django possa encontrar as URLs no arquivo urls.py do app core.
# criação de uma URL para o app core
# Toda requisição que chegar na raiz envia para a aplicação core.
# handler404 recebe uma função que retorna uma página de erro 404.


from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from core import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

handler404 = views.error404
handler500 = views.error500


# A variavel handler404 recebe a função views.error_404 e ao invés de retornar uma página de erro 404, ela retorna a página de erro 404 do core.