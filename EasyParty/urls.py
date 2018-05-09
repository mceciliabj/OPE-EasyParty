from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings

from core.views import index, contato
from core.views import detalhe_produto
from core.views import registrar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name="index"),
    url(r'^$', index, name='index'),
    url(r'^login', login, { "template_name":"login.html" }, name='entrar'),
    url(r'^logout',logout, { "next_page":"index.html" }, name="sair"),
    url(r'^(?P<slug>[\w_-]+)/$', detalhe_produto),
    url(r'^contato', contato, name="contato"),
    url(r'^registrar',registrar, name = 'registrar') # pagina de cadastro
]

# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório 
#root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)