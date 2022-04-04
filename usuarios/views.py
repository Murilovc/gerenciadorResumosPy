from django.contrib import messages
import os
import random
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import BaseDetailView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from .models import Reeducando, Relatorio, Resumo, User
#from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
#serve para redirecionar página
from django.contrib.auth.mixins import LoginRequiredMixin
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
@login_required(login_url='/login/')
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        username = nome+str(random.randint(1, 9999))
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nivel = request.POST.get('nivel')

        user = User.objects.filter(email=email).first()

        if user:
            messages.error(request, "Este email já está sendo utilizado!")

        else:

            if nivel == '1':
                user = User.objects.create_user(first_name=nome, username=username, email=email, password=senha, nivel=nivel, is_staff=1, is_superuser=1)
                user.save()
                return redirect('../usuarios/listagem/')
            
            user = User.objects.create_user(first_name=nome, username=username, email=email, password=senha, nivel=nivel)
            user.save()

            return redirect('../usuarios/listagem/')
    return redirect('/cadastro/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(email=email).first()
        if user is not None:
            
            user = authenticate(username=user.username, password=senha)
            login_django(request, user)
            return redirect('/')
        else:
            messages.error(request, "Email ou senha inválidos. Por favor, tente novamente.")

    return redirect('/login/')

def logout(request):
    logout_django(request)
    return redirect('/')


# pagina listagem - R
class ListagemUsuario(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'cadastros/listar_usuarios.html'

# pagina editar - U
class UpdateUsuario(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    fields = ['username', 'email', 'nivel']
    template_name = 'cadastros/index_usuarios.html'
    success_url = reverse_lazy('listagem')

# pagina deletar - D
class DeleteUsuario(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'cadastros/excluir_usuarios.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('listagem')


'''-----------------------------------------------
-------------------REEDUCANDO---------------------
--------------------------------------------------'''

class ListagemReeducando(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Reeducando
    template_name = 'reeducandos/listar_reeducandos.html'
    
    
class CadastroReeducando(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Reeducando
    fields = ['nome','rgc',]
    template_name = 'reeducandos/index_reeducandos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('reeducando_listagem')
    
    
class UpdateReeducando(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Reeducando
    fields = "__all__"
    template_name = 'reeducandos/index_reeducandos.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('reeducando_listagem')
    
    
class ExclusaoReeducando(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Reeducando
    template_name = 'reeducandos/excluir_reeducandos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('reeducando_listagem')




'''-----------------------------------------------
-------------------RESUMO-------------------------
--------------------------------------------------'''

class ListagemResumo(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Resumo
    template_name = 'resumos/listar_resumos.html'
    
    
class CadastroResumo(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Resumo
    fields = ['data','titulo','arquivo', 'reeducando',]
    template_name = 'resumos/index_resumos.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('resumo_listagem')
    
    
class UpdateResumo(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Resumo
    fields = "__all__"
    template_name = 'resumos/index_resumos.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('resumo_listagem')
    
    
class ExclusaoResumo(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
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

class ListagemRelatorio(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Relatorio
    template_name = 'relatorios/listar_relatorios.html'
      
    
class ExclusaoRelatorio(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
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
@login_required(login_url='/login/')
def abertura_modelform(request):
    return render(request, "index.html")


'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma tabela para que o avaliador possa escolher
quais resumos serão adicionados a fila de correção dele.
'''
class AdicaoResumoParaAvaliador(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Resumo
    template_name = 'adicao_resumos.html'
    

'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma tabela que lista e exibe o status de todos os
resumos da fila de correção do avaliador junto com um 
botão "avaliar" para o avaliador selecionar.
'''
class SalaCorrecao(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Resumo
    template_name = 'sala_correcao.html'


'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma lista de relatórios que foram feitos pelo
avaliador que está logado.

Semelhante ao ListagemRelatorio
'''   
class HistoricoRelatorioAvaliador(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Relatorio
    template_name = 'relatorios_por_avaliador.html'
    
'''
Página acessível apenas ao Usuário do tipo Avaliador.
Exibe uma visualização do pdf do resumo, junto com caixas
de seleção e de texto para o avaliador pontuar o resumo,
produzindo assim o relatório.

É o CadastroRelatorio
'''

class Corretor(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Relatorio
    template_name = 'corretor.html'
    fields = ['nota_conteudo','nota_estrutura','nota_ortografia', 'comentario',]
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('sala_correcao')
    
    '''Provável que não esteja funcionando'''
    def get_object(self, queryset=None):
        resumo = None
        id = self.kwargs.get(self.pk_url_kwarg)
        
        if id is not None:
            # Busca o resumo apartir do id
            resumo = Resumo.objects.filter(id=id).first()
            
        return resumo
    


'''
Página acessível apenas ao Usuário do tipo Diretor.
Exibe uma lista de todos os relatórios não aprovados,
junto com o botão "aprovar".

Semelhante ao ListagemRelatorio
''' 
class AprovacaoRelatorioParaDiretor(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Relatorio
    template_name = 'relatorios_por_diretor.html'


'''
Página que faz o update do status do relatório
quando o Diretor clica no botão "aprovar" na página
de aprovação de relatório
'''
class UpdateStatusRelatorio(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Relatorio
    fields = ['status',]
    template_name = 'relatorios/update_status_relatorio.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('aprovacao-relatorio')
    

class CadastroResumoPorEstagiario(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
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
@login_required(login_url='/login/')
@xframe_options_exempt
def pdf_view(request):
    try:
        return FileResponse(open('media_cdn/media/Certificado_Nacional_de_Covid-19.pdf_9P07O8b.PDF', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


