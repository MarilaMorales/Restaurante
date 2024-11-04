from rest_framework import serializers
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden, Restaurante
from .models import Resena, Menu_Dia, Pago, Empleado, Proveedor, Producto, Promociones,Direccion
from django.contrib.auth.models import User




class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'
        
class Menu_DiaSerializer(serializers.ModelSerializer):
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

    # def create(self, validated_data):
    #     # Asigna un rol por defecto si no se proporciona
    #     validated_data['rol'] = validated_data.get('rol', 'user')
    #     return super().create(validated_data)

              
    def validate_Nombre_Usuario (self, value):
        if Usuario.objects.filter(username =value).exists():
            raise serializers.ValidationError("Ya existe un usuario con este nombre.")
        return value
        
                      
    def validate_correo (self, value):
        if Usuario.objects.filter(email =value).exists():
            raise serializers.ValidationError("Ya existe un correo con este nombre.")
        return value
        
        
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '_all_'
    
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

        
class Detalles_ordenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles_orden
        fields = '__all__'


#codificacion de contraseña c 

# class RegistroSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "password")

#     def create(self, validated_data):
#         usuario = User(**validated_data)
#         usuario.set_password(validated_data['password'])  # Codifica la contraseña
#         usuario.save()  # Guarda el usuario
#         return usuario




class RegistroSerializer(serializers.ModelSerializer):
    is_staff = serializers.ChoiceField(choices=[0, 1])
   
    class Meta:
        model = User
        fields = ( "first_name", "last_name", "email", "username",  "password", "is_staff")

    def create(self, validated_data):
        # Extraer is_staff del validated_data
        is_staff = validated_data.get('is_staff', 0)  # Valor por defecto 0 

        usuario = User(**validated_data)
        usuario.set_password(validated_data['password']) 

        # Asignar el valor correcto a is_staff
        usuario.is_staff = is_staff == 1  # Admin
        usuario.save()  
        

        return usuario

