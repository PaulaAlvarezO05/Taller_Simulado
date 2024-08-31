from rest_framework import serializers 
from .models import * 

class AutorSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Autor
        fields = ('__all__')