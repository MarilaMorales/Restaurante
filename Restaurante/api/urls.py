from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaListCreate.as_view(), name='Categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='Categorias-detail'),
    
    path('administrador/', views.AdministradorListCreate.as_view(), name='reservas-list'),
    path('administrador/<int:pk>/', views.AdministradorDetail.as_view(), name='reservas-detail'),
    
    path('menu/', views.MenuListCreate.as_view(), name='Menu-list'),
    path('menu/<int:pk>/', views.MenuDetail.as_view(), name='Menu-detail'),
    
    path('usuario/', views.UsuarioListCreate.as_view(), name='Usuario-list'),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view(), name='Usuario-detail'),

    path('orden/', views.OrdenListCreate.as_view(), name='Orden-list'),
    path('orden/<int:pk>/', views.OrdenDetail.as_view(), name='Orden-detail'),

    path('detalles_orden/', views.Detalles_ordenListCreate.as_view(), name='Detalles_orden-list'),
    path('detalles_orden/<int:pk>/', views.Detalles_ordenDetail.as_view(), name='Detalles_orden-detail'),
]