from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    def validate(self, data):
        if data['Nombre_Categoria'] is None:
            raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
        return data