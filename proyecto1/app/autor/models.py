from django.db import models

# Create your models here.
class Autor(models.Model):
    class Meta: 
        verbose_name = "Autor" 
        verbose_name_plural = "Autores" 
    
    nombre = models.CharField("Nombre", max_length=100)
