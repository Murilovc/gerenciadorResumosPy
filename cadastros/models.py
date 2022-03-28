from django.db import models
from email.policy import default
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from gerenciadorResumosPy import settings


class Usuario(models.Model):
    
    nome = models.CharField('Digite seu nome', max_length=200 )
    email = models.EmailField('Digite seu email', max_length=200, unique=True)
    #aprender a usar models.IntegerChoices() aqui embaixo
    NIVEL = (
        (4, 'Avaliador'),
        (3, 'Diretor'),
        (2, 'Estagiário'),
        (1, 'Administrador'),
        
    )
    nivel = models.IntegerField(
        choices=NIVEL,
        blank=True, default=1)
    senha = models.CharField('Digite a senha', max_length=200)

    def __str__(self):
        return self.nome
    
    
class UsuarioDjango(AbstractUser):
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    def __str__(self):
        return self.usuario  
     

class Reeducando(models.Model):
    nome = models.CharField('Nome do reeducando', max_length=200)
    rgc = models.CharField('Nº do RGC', max_length=200)
    
    def __str__(self):
        return self.rgc
    
class Resumo(models.Model):
    data = models.DateField(default=datetime.now)
    titulo = models.CharField('Título do resumo', max_length=200, default='titulo')
    arquivo = models.FileField(upload_to='media')
    reeducando = models.ForeignKey(Reeducando, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.titulo
    
class Relatorio(models.Model):
    nota_conteudo = models.DecimalField('Nota conteudo', max_digits=4, decimal_places=2)
    nota_estrutura = models.DecimalField('Nota estrutura', max_digits=4, decimal_places=2)
    nota_ortografia = models.DecimalField('Nota otografia', max_digits=4, decimal_places=2)
    
    STATUS = (
        (3, 'Reprovado'),
        (2, 'Aprovado'),
        (1, 'Pendente'),       
    )
    status = models.IntegerField(
        choices=STATUS,
        blank=True, default=1)
    
    comentario = models.CharField('Comentário', max_length=200)
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    resumo = models.ForeignKey(Resumo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.status


