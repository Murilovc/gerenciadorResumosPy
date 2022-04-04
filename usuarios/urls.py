from django.urls import path
from . import views
from usuarios.views import AdicaoResumoParaAvaliador, AprovacaoRelatorioParaDiretor, CadastroReeducando, CadastroResumo, CadastroResumoPorEstagiario, Corretor, ExclusaoReeducando, ExclusaoRelatorio, ExclusaoResumo, HistoricoRelatorioAvaliador, ListagemReeducando, ListagemRelatorio, ListagemResumo, ListagemUsuario, SalaCorrecao, UpdateReeducando, UpdateResumo, UpdateStatusRelatorio, UpdateUsuario, DeleteUsuario

urlpatterns = [
    path('', views.abertura_modelform, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
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
    path('relatorios/exclusao/<int:pk>', ExclusaoRelatorio.as_view(), name='relatorio_exclusao'),
    
    # Páginas do resto do site
    
    #avaliador
    path('sala-correcao/', SalaCorrecao.as_view(), name='sala_correcao'),
    path('escolha-resumo/', AdicaoResumoParaAvaliador.as_view(), name='escolha_resumo'),
    path('corretor/<int:pk>', Corretor.as_view(), name='corretor'),
    path('historico-de-relatorio/', HistoricoRelatorioAvaliador.as_view(), name='historico_relatorio'),
    
    #diretor
    path('aprovacao-de-relatorio/', AprovacaoRelatorioParaDiretor.as_view(), name='aprovacao_relatorio'),
    path('update-status-relatorio/<int:pk>', UpdateStatusRelatorio.as_view(), name='update-relatorio'),
    
    #estagiário
    path('resumos/upload-resumo/', CadastroResumoPorEstagiario.as_view(), name='upload-resumo'),
    
    #visualizador de pdf
    #path('visualizador/', VisualizadorResumo.as_view(), name='visualizador_resumo'),
    path('visualizador/<int:pk>', views.pdf_view, name='visualizador'),
    

]