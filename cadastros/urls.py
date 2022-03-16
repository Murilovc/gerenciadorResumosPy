from django.urls import path
from cadastros import views
from cadastros.views import CadastroReeducando, CadastroRelatorio, CadastroResumo, CadastroUsuario, ExclusaoReeducando, ExclusaoRelatorio, ExclusaoResumo, ListagemReeducando, ListagemRelatorio, ListagemResumo, ListagemUsuario, UpdateReeducando, UpdateRelatorio, UpdateResumo, UpdateUsuario, DeleteUsuario


urlpatterns = [
    path('', views.abertura_modelform, name='index'),
    path('usuarios/cadastros/', CadastroUsuario.as_view(), name='cadastro'),
    path('usuarios/listagem/', ListagemUsuario.as_view(), name='listagem'),
    path('usuarios/update/<int:pk>', UpdateUsuario.as_view(), name='update'),
    path('usuarios/deletar/<int:pk>', DeleteUsuario.as_view(), name='deletar'),
    # Os apelidos dos links já estão criados, mas as páginas não,
    # por isso estes estão redirecionando para o início
    path('usuarios/reeducandos/', ListagemReeducando.as_view(), name='reeducando_listagem'),
    path('usuarios/reeducando/', CadastroReeducando.as_view(), name='reeducando_cadastro'),
    path('usuarios/reeducando/', UpdateReeducando.as_view(), name='reeducando_update'),
    path('usuarios/reeducando/', ExclusaoReeducando.as_view(), name='reeducando_exclusao'),

    path('usuarios/resumos/', ListagemResumo.as_view(), name='resumo_listagem'),
    path('usuarios/resumos/', CadastroResumo.as_view(), name='resumo_cadastro'),
    path('usuarios/resumos/', UpdateResumo.as_view(), name='resumo_update'),
    path('usuarios/resumos/', ExclusaoResumo.as_view(), name='resumo_exclusao'),

    path('usuarios/relatorios/', ListagemRelatorio.as_view(), name='relatorio_listagem'),
    path('usuarios/relatorios/', CadastroRelatorio.as_view(), name='relatorio_cadastro'),
    path('usuarios/relatorios/', UpdateRelatorio.as_view(), name='relatorio_update'),
    path('usuarios/relatorios/', ExclusaoRelatorio.as_view(), name='relatorio_exclusao'),
]