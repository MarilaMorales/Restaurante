from rest_framework import generics
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden, Resena, Especialidad
from. models import Pago, Empleado, Producto, Proveedor, Promociones, Administrador, Direccion, Restaurante
from .serializers import CategoriaSerializer, AdministradorSerializer, MenuSerializer,UsuarioSerializer
from .serializers import OrdenSerializer, Detalles_ordenSerializer, ResenaSerializer, EspecialidadSerializer
from .serializers import PagoSerializer, EmpleadoSerializer, ProductoSerializer, ProveedorSerializer, PromocionesSerializer
from .serializers import AdministradorSerializer, DireccionSerializer, RestauranteSerializer


# Reseña

class ResenaListCreate(generics.ListCreateAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class ResenaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer, 


# Especialidades

class EspecialidadListCreate(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    
    

# Pago
class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


# Empleado
class EmpleadoListCreate(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


    
    
#Proveedor

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer



# Productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    
# Promociones

class PromocionesListCreate(generics.ListCreateAPIView):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer

class PromocionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer
    

# Administradores 

class AdministradorListCreate(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class AdministradorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer



#Direccion

class DireccionListCreate(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DireccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer



# Categoria
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    
    
#Restaurante

class RestauranteListCreate(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer


# Usuario

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer    
    
    
# Orden

class OrdenListCreate(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
 

# Menu

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
        

# Detalles_Orden

class Detalles_ordenListCreate(generics.ListCreateAPIView):
    queryset = Detalles_orden.objects.all()
    serializer_class = Detalles_ordenSerializer

class Detalles_ordenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = Detalles_ordenSerializer