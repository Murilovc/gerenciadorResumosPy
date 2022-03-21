from django.urls import path
from cadastros import views
from cadastros.views import AdicaoResumoParaAvaliador, AprovacaoRelatorioParaDiretor, CadastroReeducando, CadastroResumo, CadastroUsuario, Corretor, ExclusaoReeducando, ExclusaoRelatorio, ExclusaoResumo, HistoricoRelatorioAvaliador, ListagemReeducando, ListagemRelatorio, ListagemResumo, ListagemUsuario, Login, SalaCorrecao, UpdateReeducando, UpdateResumo, UpdateUsuario, DeleteUsuario


urlpatterns = [
    path('', views.abertura_modelform, name='index'),
    
    # Páginas da área administrativa
    path('usuarios/cadastros/', CadastroUsuario.as_view(), name='cadastro'),
    path('usuarios/listagem/', ListagemUsuario.as_view(), name='listagem'),
    path('usuarios/update/<int:pk>', UpdateUsuario.as_view(), name='update'),
    path('usuarios/deletar/<int:pk>', DeleteUsuario.as_view(), name='deletar'),

    path('reeducandos/listagem/', ListagemReeducando.as_view(), name='reeducando_listagem'),
    path('reeducandos/cadastro/', CadastroReeducando.as_view(), name='reeducando_cadastro'),
    path('reeducandos/update/<int:pk>', UpdateReeducando.as_view(), name='reeducando_update'),
    path('reeducandos/exclusao/<int:pk>', ExclusaoReeducando.as_view(), name='reeducando_exclusao'),

    path('resumos/listagem/', ListagemResumo.as_view(), name='resumo_listagem'),
    path('resumos/cadastro/', CadastroResumo.as_view(), name='resumo_cadastro'),
    path('resumos/update/<int:pk>', UpdateResumo.as_view(), name='resumo_update'),
    path('resumos/exclusao/<int:pk>', ExclusaoResumo.as_view(), name='resumo_exclusao'),

    path('relatorios/listagem/', ListagemRelatorio.as_view(), name='relatorio_listagem'),
    path('relatorios/listagem/<int:pk>', ExclusaoRelatorio.as_view(), name='relatorio_exclusao'),
    
    # Páginas do resto do site
    path('sala-correcao', SalaCorrecao.as_view(), name='sala_correcao'),
    path('escolha-resumo', AdicaoResumoParaAvaliador.as_view(), name='escolha_resumo'),
    path('corretor/<int:pk>', Corretor.as_view(), name='corretor'),
    path('historico-de-relatorio', HistoricoRelatorioAvaliador.as_view(), name='historico_relatorio'),
    path('aprovacao-de-relatorio', AprovacaoRelatorioParaDiretor.as_view(), name='aprovacao_relatorio'),
    
    #Login e Logout
    path('login', Login.as_view(), name='login'),
]