from django.urls import path
from users.views import CadastroUsuario
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path('cadastros/', views.CadastroUsuario.as_view(), name='cadastro'),
]