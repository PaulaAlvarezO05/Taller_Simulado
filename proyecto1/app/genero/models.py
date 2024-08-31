from django.db import models
from ..Genero.models import Genero

class Genero (models.Model):
    class Meta:
        verbose_name='Genero'
        verbose_name_plural='Genero'
    
    Tipo=models.CharField('Tipo', max_length=100)
    
    Genero=models.ForeignKey(
        Genero,
        verbose_name='Genero',
        on_delete=models.CASCADE,
        null=True,
        blank=True

    )
    