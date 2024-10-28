from django.urls import path
from . import views

urlpatterns = [
    path('resena/', views.ResenaListCreate.as_view(), name='resena-list'),
    path('resena/<int:pk>/', views.ResenaDetail.as_view(), name='resena-detail'),
    
    path('especialidad/', views.EspecialidadListCreate.as_view(), name='Especialidad-list'),
    path('especialidad/<int:pk>/', views.EspecialidadDetail.as_view(), name='Especialidad-detail'),
    
    path('pago/', views.PagoListCreate.as_view(), name='Pago-list'),
    path('pago/<int:pk>/', views.PagoDetail.as_view(), name='Pago-detail'),
    
    path('empleado/', views.EmpleadoListCreate.as_view(), name='Empleado-list'),
    path('empleado/<int:pk>/', views.EmpleadoDetail.as_view(), name='Empleado-detail'),
    
    path('proveedor/', views.ProductoListCreate.as_view(), name='Producto-list'),
    path('proveedor/<int:pk>/', views.ProductoDetail.as_view(), name='Producto-detail'),
    
    path('producto/', views.ProveedorListCreate.as_view(), name='Proveedor-list'),
    path('producto/<int:pk>/', views.ProveedorDetail.as_view(), name='Proveedor-detail'),
    
    path('promociones/', views.PromocionesListCreate.as_view(), name='Promociones-list'),
    path('promociones/<int:pk>/', views.PromocionesDetail.as_view(), name='Promociones-detail'),
    
    path('administrador/', views.AdministradorListCreate.as_view(), name='reservas-list'),
    path('administrador/<int:pk>/', views.AdministradorDetail.as_view(), name='reservas-detail'),
    
    path('Direccion/', views.DireccionListCreate.as_view(), name='Direccion-list'),
    path('Direccion/<int:pk>/', views.DireccionDetail.as_view(), name='Direccion-detail'),
    
    path('categorias/', views.CategoriaListCreate.as_view(), name='Categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='Categorias-detail'),
    
    path('restaurante/', views.RestauranteListCreate.as_view(), name='Restaurante-list'),
    path('restaurante/<int:pk>/', views.RestauranteDetail.as_view(), name='Restaurante-detail'),
    
    path('usuario/', views.UsuarioListCreate.as_view(), name='Usuario-list'),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view(), name='Usuario-detail'),
    
    path('orden/', views.OrdenListCreate.as_view(), name='Orden-list'),
    path('orden/<int:pk>/', views.OrdenDetail.as_view(), name='Orden-detail'),
    
    path('menu/', views.MenuListCreate.as_view(), name='Menu-list'),
    path('menu/<int:pk>/', views.MenuDetail.as_view(), name='Menu-detail'),

    path('detalles_orden/', views.Detalles_ordenListCreate.as_view(), name='Detalles_orden-list'),
    path('detalles_orden/<int:pk>/', views.Detalles_ordenDetail.as_view(), name='Detalles_orden-detail'),
]
