from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from users.models import Usuario



class HomePageView(TemplateView):
    template_name = "home.html"

class CadastroUsuario(CreateView):
    model = Usuario
    fields = ['email','nivel','password']
    template_name = 'cadastros/index_usuarios.html'
    #success_url = reverse_lazy('listagem')