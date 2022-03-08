from django.db import models
from datetime import date

class Livros(models.Model):
    nome = models.CharField(max_length= 100)
    autor = models.CharField(max_length= 50)
    co_autor = models.CharField(max_length= 50, blank = True, null = True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default=False, blank = True)
    nome_emprestado = models.CharField(max_length=100, blank = True, null = True)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    tempo_duracao = models.DateField(blank = True, null = True)

    class Meta:
        verbose_name = "Livro"