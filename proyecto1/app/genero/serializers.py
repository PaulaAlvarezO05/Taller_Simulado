from rest_framework import serializers 
from .models import * 

class GeneroSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Genero
        fields = ('__all__')