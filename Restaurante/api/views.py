from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden, Menu_Dia, Resena
from. models import Pago, Empleado, Producto, Proveedor, Promociones, Administrador, Direccion, Restaurante
from .serializers import CategoriaSerializer, AdministradorSerializer, MenuSerializer,UsuarioSerializer
from .serializers import OrdenSerializer, Detalles_ordenSerializer, ResenaSerializer
from .serializers import PagoSerializer, EmpleadoSerializer, ProductoSerializer, ProveedorSerializer, PromocionesSerializer
from .serializers import AdministradorSerializer, DireccionSerializer, RestauranteSerializer, Menu_DiaSerializer


# Reseña

class ResenaListCreate(generics.ListCreateAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permission_classes = [IsAuthenticated]
    

class ResenaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permission_classes = [IsAuthenticated] 


# Especialidades

class Menu_DiaListCreate(generics.ListCreateAPIView):
    queryset = Menu_Dia.objects.all()
    serializer_class = Menu_DiaSerializer
 

class Menu_DiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu_Dia.objects.all()
    serializer_class = Menu_DiaSerializer

    
    

# Pago
class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]


# Empleado
class EmpleadoListCreate(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]


    
    
#Proveedor

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]



# Productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    
    
# Promociones

class PromocionesListCreate(generics.ListCreateAPIView):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer
    permission_classes = [IsAuthenticated]

class PromocionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer
    permission_classes = [IsAuthenticated]
    

# Administradores 

class AdministradorListCreate(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [IsAuthenticated]

class AdministradorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [IsAuthenticated]



#Direccion

class DireccionListCreate(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticated]

class DireccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticated]



# Categoria
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
    
    
#Restaurante

class RestauranteListCreate(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    permission_classes = [IsAuthenticated]

class RestauranteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    permission_classes = [IsAuthenticated]


# Usuario

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]


##### Usuario Consulta

class UsuarioListDes(generics.ListAPIView):
    queryset = Usuario.objects.all()
    Usuario_ordenados_desc = Usuario.objects.filter().order_by('-Nombre_Usuario')
    serializer_class = UsuarioSerializer



    
    
    
# Orden

class OrdenListCreate(generics.ListCreateAPIView):
    serializer_class = OrdenSerializer

    def get_queryset(self):
        queryset = Orden.objects.all()
        estado = self.request.query_params.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset

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
    permission_classes = [IsAuthenticated]

class Detalles_ordenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = Detalles_ordenSerializer
    permission_classes = [IsAuthenticated]
    
    
    
