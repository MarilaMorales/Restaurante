
from rest_framework import serializers
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden, Restaurante
from .models import Resena, Especialidad, Pago, Empleado, Proveedor, Producto, Promociones,Direccion

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '_all_'
        
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '_all_'
        
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '_all_'
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '_all_'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '_all_'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '_all_'

class PromocionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones
        fields = '_all_'
        
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '_all_'
        
    def validate_nombre_admin(self, value):
        if Administrador.objects.filter(nombre_admin=value).exists():
            raise serializers.ValidationError("Ya existe un Administrador con este nombre.")
        return value

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '_all_'

       
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '_all_'
        
              
class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '_all_'
        

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '_all_'
        
              
    def validate_Nombre_Usuario (self, value):
        if Usuario.objects.filter(Nombre_Usuario =value).exists():
            raise serializers.ValidationError("Ya existe un usuario con este nombre.")
        return value
        
        
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '_all_'

    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '_all_'

        
class Detalles_ordenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles_orden
        fields = '_all_'




