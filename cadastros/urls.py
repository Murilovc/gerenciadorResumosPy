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
    path('reeducandos/listagem/', ListagemReeducando.as_view(), name='reeducando_listagem'),
    path('reeducandos/cadastro/', CadastroReeducando.as_view(), name='reeducando_cadastro'),
    path('reeducandos/update/<int:pk>', UpdateReeducando.as_view(), name='reeducando_update'),
    path('reeducandos/exclusao/<int:pk>', ExclusaoReeducando.as_view(), name='reeducando_exclusao'),

    path('resumos/listagem/', ListagemResumo.as_view(), name='resumo_listagem'),
    path('resumos/cadastro/', CadastroResumo.as_view(), name='resumo_cadastro'),
    path('resumos/update/<int:pk>', UpdateResumo.as_view(), name='resumo_update'),
    path('resumos/exclusao/<int:pk>', ExclusaoResumo.as_view(), name='resumo_exclusao'),

    path('relatorios/listagem/', ListagemRelatorio.as_view(), name='relatorio_listagem'),
    path('relatorios/listagem/', CadastroRelatorio.as_view(), name='relatorio_cadastro'),
    path('relatorios/listagem/<int:pk>', UpdateRelatorio.as_view(), name='relatorio_update'),
    path('relatorios/listagem/<int:pk>', ExclusaoRelatorio.as_view(), name='relatorio_exclusao'),
]