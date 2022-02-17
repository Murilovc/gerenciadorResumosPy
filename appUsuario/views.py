from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Usuario
#serve para redirecionar página
from django.urls import reverse_lazy

# pagina cadastrar - C
class CadastroUsuario(CreateView):
    model = Usuario
    fields = ['nome','email','nivel','senha']
    template_name = 'appUsuario/index_usuarios.html'
    success_url = reverse_lazy('listagem')

# pagina listagem - R
class ListagemUsuario(ListView):
    model = Usuario
    template_name = 'appUsuario/listar_usuarios.html'

# pagina editar - U
class UpdateUsuario(UpdateView):
    model = Usuario
    fields = "__all__"
    template_name = 'appUsuario/index_usuarios.html'
    success_url = reverse_lazy('listagem')

# pagina deletar - D
class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'appUsuario/excluir_usuarios.html'
    success_url = reverse_lazy('listagem')

def abertura_modelform(request):
    return render(request, "index.html")

