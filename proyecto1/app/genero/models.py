from django.db import models

class Genero (models.Model):
    class Meta:
        verbose_name='Genero'
        verbose_name_plural='Genero'
    
    Tipo = models.CharField('Tipo', max_length=100)

    def __str__(self):
        return f'{self.Tipo}'