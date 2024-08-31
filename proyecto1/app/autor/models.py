from django.db import models

# Create your models here.
class Autor(models.Model):
    class Meta: 
        verbose_name = "Autor" 
        verbose_name_plural = "Autores" 
    
    nombre = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
