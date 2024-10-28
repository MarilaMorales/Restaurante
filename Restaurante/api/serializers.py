
from rest_framework import serializers
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden, Restaurante
from .models import Resena, Menu_Dia, Pago, Empleado, Proveedor, Producto, Promociones,Direccion

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'
        
class Menu_del_DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Dia
        fields = '__all__'
        
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PromocionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones
        fields = '__all__'
        
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'
        
    def validate_nombre_admin(self, value):
        if Administrador.objects.filter(nombre_admin=value).exists():
            raise serializers.ValidationError("Ya existe un Administrador con este nombre.")
        return value

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

       
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        
              
class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'
        

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
              
    def validate_Nombre_Usuario (self, value):
        if Usuario.objects.filter(Nombre_Usuario =value).exists():
            raise serializers.ValidationError("Ya existe un usuario con este nombre.")
        return value
        
        
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
    
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

        
class Detalles_ordenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles_orden
        fields = '__all__'




