from django.db import models
from ..autor.models import Autor 
from ..genero.models import Genero

# Create your models here.
class Libro (models.Model):
    titulo = models.CharField("Titulo", max_length=200)  
  
    idAutor = models.ForeignKey ( 
    Autor, 
    verbose_name="Autor", 
    on_delete=models.CASCADE, 
    null=True, 
    blank=True 
    ) 

    fecha =models.DateTimeField("Fecha de publicación", max_length=50)

    idGenero = models.ForeignKey ( 
    Autor, 
    verbose_name="Genero", 
    on_delete=models.CASCADE, 
    null=True, 
    blank=True 
    ) 
    disponibilidad= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.titulo}{Autor.nombre}'
    



