 
from django.urls import path
from . import views

urlpatterns = [
 
  path('categoria/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('categoria/', views.CategoriaListCreate.as_view(), name='categoria-list'),
]