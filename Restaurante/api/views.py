from rest_framework import generics
from .models import Categorias, Administrador, Menu, Usuario, Orden, Detalles_orden
from .serializers import CategoriaSerializer, AdministradorSerializer, MenuSerializer,UsuarioSerializer
from .serializers import OrdenSerializer, Detalles_ordenSerializer


# Categoria
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer, 
    
    
    
# Administrador

class AdministradorListCreate(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class AdministradorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer




# Menu

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    



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
      
# Detalles_Orden

class Detalles_ordenListCreate(generics.ListCreateAPIView):
    queryset = Detalles_orden.objects.all()
    serializer_class = Detalles_ordenSerializer

class Detalles_ordenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = Detalles_ordenSerializer