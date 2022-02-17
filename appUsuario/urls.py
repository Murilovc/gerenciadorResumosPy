from django.urls import path
from appUsuario import views
from appUsuario.views import CadastroUsuario, ListagemUsuario, UpdateUsuario, DeleteUsuario


urlpatterns = [
    path('', views.abertura_modelform, name='index'),
    path('cadastros/', CadastroUsuario.as_view(), name='cadastro'),
    path('listagem/', ListagemUsuario.as_view(), name='listagem'),
    path('update/<int:pk>', UpdateUsuario.as_view(), name='update'),
    path('deletar/<int:pk>', DeleteUsuario.as_view(), name='deletar'),
]