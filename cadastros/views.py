import os
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.views.generic.detail import BaseDetailView
from django.views.decorators.clickjacking import xframe_options_exempt

from .forms import LoginResumoForm
from .models import Reeducando, Relatorio, Resumo, Usuario
from gerenciadorResumosPy import settings
#serve para redirecionar página
from django.urls import reverse_lazy

'''
.__________________________________________________
|--------------------------------------------------|
|------------------PÁGINAS DA ÁREA-----------------|
|------------------ADMINISTRATIVA------------------|
|__________________________________________________|
'''

'''-----------------------------------------------
-------------------USUÁRIO------------------------
--------------------------------------------------'''
# pagina cadastrar - C
class CadastroUsuario(CreateView):
    model = Usuario
    fields = ['nome','email','nivel','senha']
    template_name = 'cadastros/index_usuarios.html'
    success_url = reverse_lazy('listagem')

# pagina listagem - R
class ListagemUsuario(ListView):
    model = Usuario
    template_name = 'cadastros/listar_usuarios.html'

# pagina editar - U
class UpdateUsuario(UpdateView):
    model = Usuario
    fields = "__all__"
    template_name = 'cadastros/index_usuarios.html'
    success_url = reverse_lazy('listagem')

# pagina deletar - D
class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'cadastros/excluir_usuarios.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('listagem')



'''-----------------------------------------------
----------------USUÁRIO DO DJANGO-----------------
--------------------------------------------------'''


'''-----------------------------------------------
-------------------REEDUCANDO---------------------
--------------------------------------------------'''

class ListagemReeducando(ListView):
    model = Reeducando
    template_name = 'reeducandos/listar_reeducandos.html'
    
    
class CadastroReeducando(CreateView):
    model = Reeducando
    fields = ['nome','rgc',]
    template_name = 'reeducandos/index_reeducandos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('reeducando_listagem')
    
    
class UpdateReeducando(UpdateView):
    model = Reeducando
    fields = "__all__"
    template_name = 'reeducandos/index_reeducandos.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('reeducando_listagem')
    
    
class ExclusaoReeducando(DeleteView):
    model = Reeducando
    template_name = 'reeducandos/excluir_reeducandos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('reeducando_listagem')




'''-----------------------------------------------
-------------------RESUMO-------------------------
--------------------------------------------------'''

class ListagemResumo(ListView):
    model = Resumo
    template_name = 'resumos/listar_resumos.html'
    
    
class CadastroResumo(CreateView):
    model = Resumo
    fields = ['data','titulo','arquivo', 'reeducando',]
    template_name = 'resumos/index_resumos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('resumo_listagem')
    
    
class UpdateResumo(UpdateView):
    model = Resumo
    fields = "__all__"
    template_name = 'resumos/index_resumos.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('resumo_listagem')
    
    
class ExclusaoResumo(DeleteView):
    model = Resumo
    template_name = 'resumos/excluir_resumos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('resumo_listagem')




'''-----------------------------------------------
-------------------RELATÓRIO----------------------
OBS: Na área administrativa será possível 
VISUALIZAR e EXCLUIR os relatórios, mas NÃO CRIAR
ou EDITAR, pois o ato da avaliação é exclusivo do 
Avaliador e feito debaixo de um termo de 
compromisso que o avaliador aceita.
--------------------------------------------------'''

class ListagemRelatorio(ListView):
    model = Relatorio
    template_name = 'relatorios/listar_relatorios.html'
      
    
class ExclusaoRelatorio(DeleteView):
    model = Relatorio
    template_name = 'relatorios/excluir_relatorios.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('relatorio_listagem')


'''
.__________________________________________________
|--------------------------------------------------|
|-------------PÁGINAS DO RESTO DO SITE-------------|
|--------------------------------------------------|
|__________________________________________________|
'''
def abertura_modelform(request):
    return render(request, "index.html")


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginResumoForm
    


'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma tabela para que o avaliador possa escolher
quais resumos serão adicionados a fila de correção dele.
'''
class AdicaoResumoParaAvaliador(ListView):
    model = Resumo
    template_name = 'adicao_resumos.html'
    

'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma tabela que lista e exibe o status de todos os
resumos da fila de correção do avaliador junto com um 
botão "avaliar" para o avaliador selecionar.
'''
class SalaCorrecao(ListView):
    model = Resumo
    template_name = 'sala_correcao.html'


'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma lista de relatórios que foram feitos pelo
avaliador que está logado.

Semelhante ao ListagemRelatorio
'''   
class HistoricoRelatorioAvaliador(ListView):
    model = Relatorio
    template_name = 'relatorios_por_avaliador.html'
    
'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma visualização do pdf do resumo, junto com caixas
de seleção e de texto para o avaliador pontuar o resumo,
produzindo assim o relatório.

É o CadastroRelatorio
'''
class Corretor(CreateView):
    model = Relatorio
    template_name = 'corretor.html'
    fields = ['nota_conteudo','nota_estrutura','nota_ortografia', 'comentario',]
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('sala_correcao')
    
    def get_object(self, queryset=None):
        resumo = None
        id = self.kwargs.get(self.pk_url_kwarg)
        
        if id is not None:
            # Busca o resumo apartir do id
            resumo = Resumo.objects.filter(id=id).first()
            
        return resumo
    

class UpdateResumoParaAvaliador(UpdateView):
    model = Resumo
    fields = ['avaliador']
    template_name = 'resumos/update_avaliador_resumo.html'
    success_url = reverse_lazy('escolha_resumo')
'''
Página acessível apenas ao Usuário do tipo Diretor.
Exibe uma lista de todos os relatórios não aprovados,
junto com o botão "aprovar".

Semelhante ao ListagemRelatorio
''' 
class AprovacaoRelatorioParaDiretor(ListView):
    model = Relatorio
    template_name = 'relatorios_por_diretor.html'


'''
Página que faz o update do status do relatório
quando o Diretor clica no botão "aprovar" na página
de aprovação de relatório
'''
class UpdateStatusRelatorio(UpdateView):
    model = Relatorio
    fields = ['status',]
    template_name = 'relatorios/update_status_relatorio.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('aprovacao-relatorio')
    

class CadastroResumoPorEstagiario(CreateView):
    model = Resumo
    fields = ['data','titulo','arquivo', 'reeducando',]
    template_name = 'resumos/upload_resumos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('resumo_listagem')
    
'''    
https://stackoverflow.com/questions/11779246/how-to-show-a-pdf-file-in-a-django-view
class VisualizadorResumo(BaseDetailView):
    
    template_name = 'visualizador.html'
    
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk', None) #1
        resumo = get_object_or_404(Resumo, pk=id) #2
        fname = resumo.arquivo #3
        path = os.path.join(settings.MEDIA_ROOT, 'media\\' + fname)#4
        response = FileResponse(open(path, 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename={}".format(fname)
        return response


'''
@xframe_options_exempt
def pdf_view(request):
    try:
        return FileResponse(open('media_cdn/media/Certificado_Nacional_de_Covid-19.pdf_9P07O8b.PDF', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
