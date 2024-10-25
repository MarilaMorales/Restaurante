from rest_framework import generics
from django.shortcuts import render
from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
# Categoría
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer