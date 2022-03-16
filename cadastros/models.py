from django.db import models

class Usuario(models.Model):
    
    nome = models.CharField('Digite seu nome', max_length=200 )
    email = models.EmailField('Digite seu email', max_length=200 )
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

class Reeducando(models.Model):
    nome = models.CharField('Nome do reeducando', max_length=200)
    rgc = models.CharField('Nº do RGC', max_length=200)
    
    def __str__(self):
        return self.rgc
    
class Resumo(models.Model):
    data = models.DateTimeField('Data')
    titulo = models.CharField('Título do resumo', max_length=200, default='titulo')
    arquivo = models.FilePathField()
    reeducando = models.ForeignKey(Reeducando, on_delete=models.CASCADE)
    
class Relatorio(models.Model):
    nota_conteudo = models.DecimalField('Nota conteudo', max_digits=4, decimal_places=2)
    nota_estrutura = models.DecimalField('Nota estrutura', max_digits=4, decimal_places=2)
    nota_ortografia = models.DecimalField('Nota otografia', max_digits=4, decimal_places=2)
    #aprender a usar models.TextChoices aqui em baixo
    status = models.CharField('Status',max_length=200)
    comentario = models.CharField('Comentário', max_length=200)
    #ainda falta criar a classe Avaliador
    #avaliador = models.ForeignKey(Avaliador, on_delete=models.CASCADE)
    resumo = models.ForeignKey(Resumo, on_delete=models.CASCADE)


