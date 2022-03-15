from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Reeducando, Relatorio, Resumo, Usuario
#serve para redirecionar página
from django.urls import reverse_lazy

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

def abertura_modelform(request):
    return render(request, "index.html")



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
--------------------------------------------------'''

class ListagemRelatorio(ListView):
    model = Relatorio
    template_name = 'relatorios/listar_relatorios.html'
    
    
class CadastroRelatorio(CreateView):
    model = Relatorio
    fields = ['nota_conteudo','nota_estrutura','nota_ortografia', 'status', 'comentario', 'resumo',]
    template_name = 'relatorios/index_relatorios.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('relatorio_listagem')
    
    
class UpdateRelatorio(UpdateView):
    model = Relatorio
    fields = "__all__"
    template_name = 'relatorios/index_relatorios.html'
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('relatorio_listagem')
    
    
class ExclusaoRelatorio(DeleteView):
    model = Relatorio
    template_name = 'relatorios/excluir_relatorios.html'
    
    #recebe o apelido da página que foi defino em urls.py
    success_url = reverse_lazy('relatorio_listagem')
