from rest_framework import serializers 
from .models import * 

class GeneroSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Genero
        fields = ('_all_') 