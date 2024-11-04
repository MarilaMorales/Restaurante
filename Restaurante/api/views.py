from rest_framework import generics
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegistroSerializer
from django.db.models import Count
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden, Menu_Dia, Resena
from. models import Pago, Empleado, Producto, Proveedor, Promociones, Administrador, Direccion, Restaurante
from .serializers import CategoriaSerializer, AdministradorSerializer, MenuSerializer,UsuarioSerializer
from .serializers import OrdenSerializer, Detalles_ordenSerializer, ResenaSerializer
from .serializers import PagoSerializer, EmpleadoSerializer, ProductoSerializer, ProveedorSerializer, PromocionesSerializer
from .serializers import AdministradorSerializer, DireccionSerializer, RestauranteSerializer, Menu_DiaSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import Administrador
from .serializers import AdministradorSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistroSerializer 




# Reseña

class ResenaListCreate(generics.ListCreateAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permission_classes = [AllowAny]
    

class ResenaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permission_classes = [AllowAny] 


# Especialidades

class Menu_DiaListCreate(generics.ListCreateAPIView):
    queryset = Menu_Dia.objects.all()
    serializer_class = Menu_DiaSerializer
    permission_classes = [AllowAny]
 

class Menu_DiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu_Dia.objects.all()
    serializer_class = Menu_DiaSerializer
    permission_classes = [AllowAny]

# Pago
class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [AllowAny]

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [AllowAny]


# Empleado
class EmpleadoListCreate(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]

class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]


    
    
#Proveedor

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [AllowAny]

class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [AllowAny]



# Productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]
    
    
# Promociones

class PromocionesListCreate(generics.ListCreateAPIView):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer
    permission_classes = [AllowAny]

class PromocionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer
    permission_classes = [AllowAny]
    

# Administradores 

class AdministradorListCreate(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [AllowAny]

    # def get(self, request, *args, **kwargs):
    #     return admin_middleware(super().get)(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return admin_middleware(super().post)(request, *args, **kwargs)



class AdministradorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [AllowAny]









#Direccion

class DireccionListCreate(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [AllowAny]

class DireccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [AllowAny]



# Categoria
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]
    
    
#Restaurante

class RestauranteListCreate(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    permission_classes = [AllowAny]

class RestauranteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    permission_classes = [AllowAny]


# Usuario

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    
    
  
  
class RegistroView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]
  
  

    
# class RegistroView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistroSerializer
#     permission_classes = [AllowAny]

##Cambiamos User por Usuario


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Inicia sesión al usuario
            refresh = RefreshToken.for_user(user)  # Genera tokens
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Credenciales inválidas'}, status=400)



##### Usuario Consulta


class UsuarioListDes(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.order_by('-username')


    
    
    
# Orden

class OrdenListCreate(generics.ListCreateAPIView):
    serializer_class = OrdenSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Orden.objects.all()
        estado = self.request.query_params.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset

class OrdenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    permission_classes = [AllowAny]

# Menu

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]
 
 
 ## consulta menu mas vendido 
 
# class MenuMasVendidos(generics.ListAPIView):
#     serializer_class = MenuSerializer
#     def get_queryset(self):
#         return Menu.objects.annotate(vendido_count=Count('detalles_orden__orden')).order_by('-vendido_count')[:3]
 
class MenuMasVendidos(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return (
            Menu.objects
            .annotate(vendido_count=Count('orden__detalles_orden'))
            .order_by('-vendido_count')[:3]
        )
 
 
        

# Detalles_Orden

class Detalles_ordenListCreate(generics.ListCreateAPIView):
    queryset = Detalles_orden.objects.all()
    serializer_class = Detalles_ordenSerializer
    permission_classes = [AllowAny]


class Detalles_ordenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = Detalles_ordenSerializer
    permission_classes = [AllowAny]
    
    



