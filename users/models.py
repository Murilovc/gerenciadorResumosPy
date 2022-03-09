from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    bio = models.TextField(blank=True)
    NIVEL = (
        (4, 'Avaliador'),
        (3, 'Diretor'),
        (2, 'Estagiário'),
        (1, 'Administrador'),
        
    )
    nivel = models.IntegerField(
        choices=NIVEL,
        blank=True, default=1)