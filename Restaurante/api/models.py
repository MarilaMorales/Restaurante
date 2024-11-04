from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Resena(models.Model):
    mensaje_reseña = models.CharField(max_length=20)

    def _str_(self):
        return f'{self.mensaje_reseña}'
    

class Menu_Dia(models.Model):
    Postre = models.CharField(max_length=20)
    Plato_Fuerte = models.CharField(max_length=80)
    Bebida = models.CharField(max_length=20)
    
    def _str_(self):
        return f'{self.Postre} - {self.Plato_Fuerte} - {self.Bebida}'


class Pago(models.Model):
    Metodo_pago = models.CharField(max_length=20)
    
    def _str_(self):
        return f'{self.Metodo_pago}'


class Empleado(models.Model):
    Nombre_empleado = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Codigo_empleado = models.IntegerField()

    def __str__(self):
        return f'{self.Nombre_empleado} - {self.Codigo_empleado}'

class Proveedor(models.Model):
    Nombre_Proveedor = models.CharField(max_length=20)
    Telefono = models.IntegerField()
    
    def __str__(self):
        return f'{self.Nombre_Proveedor} - {self.Telefono}'

     
class Producto(models.Model):
    ingrediente = models.CharField(max_length=25)
    stock = models.CharField(max_length=20)    
    Proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{self.stock} - {self.ingrediente}- {self.Proveedor}'



class Promociones(models.Model):
    Promocion = models.CharField(max_length=150)
     
    def __str__(self):
        return f'{self.Promocion}'



class Administrador(models.Model):
    nombre_admin = models.CharField(max_length=50)
    apellido_admin = models.CharField(max_length=50)
 
    def __str__(self):
        return f'{self.nombre_admin} - {self.apellido_admin}' 


class Direccion (models.Model):
    Canton = models.CharField(max_length=100)
    Distrito = models.CharField(max_length=100)
    Provincia = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.Canton} - {self.Distrito} - {self.Provincia}'



class Categorias(models.Model):
    Nombre_Categoria = models.CharField(max_length=50, default="Sin Categoría")


    def _str_(self):
        return f'{self.Nombre_Categoria}' 
    


class Restaurante (models.Model):
    Direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    mensaje_reseña = models.ForeignKey('Resena', on_delete=models.CASCADE)
    Administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Direccion} - {self.mensaje_reseña} - {self.Administrador}'
    


class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):  
        return f'{self.usuario}'









# class Usuario(models.Model):
#     Nombre_Usuario = models.CharField(max_length=100, unique=True)
#     apellido_usuario = models.CharField(max_length=100)
#     password= models.CharField(max_length=60, default="Sin Categoría")
#     correo = models.CharField(max_length=20)
    
    
#     def _str_(self):  
#         return f'{self.Nombre_Usuario} - {self.apellido_usuario} - {self.correo}'







class Menu(models.Model):
    Plato = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    Promocion = models.ForeignKey('Promociones', on_delete=models.CASCADE)
    Plato_Del_Dia = models.ForeignKey('Menu_Dia', on_delete=models.CASCADE)
    Categorias = models.ForeignKey('Categorias', on_delete=models.CASCADE)
 
    def _str_(self):
        return f'{self.Plato} - {self.Descripcion} - {self.precio} - {self.Promocion} - {self.Plato_Del_Dia} - {self.Categorias}' 
    

class Orden(models.Model):
    ESTADO_ORDEN=[
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
        ('entregado', 'Entregado'),
    ]

    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_ORDEN)
    Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    Empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    Menu = models.ForeignKey('Menu', on_delete=models.CASCADE)    
    
    
    def __str__(self):
        return f'{self.fecha} - {self.estado} - {self.Usuario} - {self.Empleado} - {self.Menu}'



class Detalles_orden(models.Model):
    Orden = models.ForeignKey('Orden', on_delete=models.CASCADE)
    Pago = models.ForeignKey('Pago', on_delete=models.CASCADE)
    Restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Total = models.IntegerField()

    def _str_(self):
        return f'{self.Orden} - {self.Pago} - {self.Restaurante} - {self.Cantidad} - {self.Total} '
        

    
