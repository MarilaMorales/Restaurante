
from django.db import models

# Create your models here.

class Resena(models.Model):
    mensaje_reseña = models.CharField(max_length=20)

    def __str__(self):
        return self.mensaje_reseña
    

class Especialidad(models.Model):
    Plato_Del_Dia = models.CharField(max_length=20)

    def __str__(self):
        return self.Plato_Del_Dia


class Pago(models.Model):
    Metodo_pago = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Metodo_pago


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
        return self.Promocion



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
    Entrada = models.CharField(max_length=20)
    Postre = models.CharField(max_length=20)
    Plato_Fuerte = models.CharField(max_length=20)
    Bebida = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.Entrada} - {self.Postre} - {self.Plato_Fuerte} - {self.Bebida}' 
    


class Restaurante (models.Model):
    Direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    Resena = models.ForeignKey('Reseña', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Direccion} - {self.Resena}'
    

class Usuario(models.Model):
    Nombre_Usuario = models.CharField(max_length=100, unique=True)
    apellido_usuario = models.CharField(max_length=100)
    correo = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.Nombre_Usuario} - {self.apellido_usuario} - {self.correo}'


class Orden(models.Model):
    ESTADO_ORDEN=[
        ('en_proceso', 'En Proceso')
        ('finalizado', 'Finalizado')
        ('entregado', 'Entregado')
    ]

    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_ORDEN)
    Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    Administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.fecha} - {self.estado} - {self.Usuario}'



class Menu(models.Model):
    Plato = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    Promocion = models.ForeignKey('Promociones', on_delete=models.CASCADE)
    Plato_Del_Dia = models.ForeignKey('Espacialidad', on_delete=models.CASCADE)
    Categorias = models.ForeignKey('Categorias', on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.Platolato} - {self.Descripcion} - {self.precio} - {self.Categorias}' 
    


class Detalles_orden(models.Model):
    Orden = models.ForeignKey('Orden', on_delete=models.CASCADE)
    Menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    Pago = models.ForeignKey('Pago', on_delete=models.CASCADE)
    Empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Total = models.IntegerField()

    def __str__(self):
        return f'{self.Orden} - {self.Menu} - {self.Cantidad} - {self.Total}'
        

    
