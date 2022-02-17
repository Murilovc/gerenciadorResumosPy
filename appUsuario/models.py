from django.db import models

class Usuario(models.Model):
    nome = models.CharField('Digite seu nome', max_length=200 )
    email = models.EmailField('Digite seu email', max_length=200 )
    #aprender a usar models.IntegerChoices() aqui embaixo
    nivel = models.IntegerField('Digite o nível de privilégio');
    senha = models.CharField('Digite a senha', max_length=200)
    
    def __str__(self):
        return self.nome

