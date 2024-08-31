from rest_framework import serializers 
from .models import * 

class AutorSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Autor
        fields = ('_all_') 