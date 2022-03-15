from django.urls import path
from cadastros import views
from cadastros.views import CadastroReeducando, CadastroResumo, CadastroUsuario, ExclusaoReeducando, ListagemReeducando, ListagemRelatorio, ListagemResumo, ListagemUsuario, UpdateReeducando, UpdateUsuario, DeleteUsuario


urlpatterns = [
    path('', views.abertura_modelform, name='index'),
    path('usuarios/cadastros/', CadastroUsuario.as_view(), name='cadastro'),
    path('usuarios/listagem/', ListagemUsuario.as_view(), name='listagem'),
    path('usuarios/update/<int:pk>', UpdateUsuario.as_view(), name='update'),
    path('usuarios/deletar/<int:pk>', DeleteUsuario.as_view(), name='deletar'),
    # Os apelidos dos links já estão criados, mas as páginas não,
    # por isso estes estão redirecionando para o início
    path('', ListagemReeducando.as_view(), name='reeducando_listagem'),
    path('', CadastroReeducando.as_view(), name='reeducando_cadastro'),
    path('', UpdateReeducando.as_view(), name='reeducando_update'),
    path('', ExclusaoReeducando.as_view(), name='reeducando_exclusao'),
    path('', ListagemResumo.as_view(), name='resumo_listagem'),
    path('', CadastroResumo.as_view(), name='resumo_cadastro'),
    path('', UpdateReeducando.as_view(), name='resumo_update'),
    path('', ExclusaoReeducando.as_view(), name='resumo_exclusao'),
    path('', ListagemRelatorio.as_view(), name='relatorio_listagem'),
]