from django.db import models
from email.policy import default
from django.contrib.auth.models import AbstractUser
from datetime import datetime
#from django.contrib.auth.models import User


        

class User(AbstractUser):
    NIVEL = (
        (4, 'Avaliador'),
        (3, 'Diretor'),
        (2, 'Estagiário'),
        (1, 'Administrador'),
        
    )
    nivel = models.IntegerField(
        choices=NIVEL,
        blank=True, default=1)

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
    avaliador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.titulo
    
class Relatorio(models.Model):
    
    CONTEUDO = (
        (0.0,'0.0'),
        (0.5,'0.5'),
        (1.0,'1.0'),
        (1.5,'1.5'),
        (2.0,'2.0'),
        (2.5,'2.5'),
        (3.0,'3.0'),
        (3.5,'3.5'),
        (4.0,'4.0'),
        (4.5,'4.5'),
        (5.0,'5.0'),
    )
    
    ESTRUTURA = (
        (0.0,'0.0'),
        (0.5,'0.5'),
        (1.0,'1.0'),
        (1.5,'1.5'),
        (2.0,'2.0'),
    )
    
    ORTOGRAFIA = (
        (0.0,'0.0'),
        (0.5,'0.5'),
        (1.0,'1.0'),
        (1.5,'1.5'),
        (2.0,'2.0'),
        (2.5,'2.5'),
        (3.0,'3.0'),
    )
    
    nota_conteudo = models.DecimalField('Nota conteudo', choices=CONTEUDO, max_digits=2, decimal_places=1)
    nota_estrutura = models.DecimalField('Nota estrutura', choices=ESTRUTURA, max_digits=2, decimal_places=1)
    nota_ortografia = models.DecimalField('Nota ortografia', choices=ORTOGRAFIA, max_digits=2, decimal_places=1)
    
    STATUS = (
        (3, 'Reprovado'),
        (2, 'Aprovado'),
        (1, 'Pendente'),       
    )
    status = models.IntegerField(
        choices=STATUS,
        blank=True, default=1)
    
    comentario = models.CharField('Comentário', max_length=200, null=True, blank=True)
    avaliador = models.ForeignKey(User, on_delete=models.CASCADE)
    resumo = models.ForeignKey(Resumo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.status