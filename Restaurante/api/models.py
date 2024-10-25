from django.db import models

# Create your models here.


class Categorias(models.Model):
    Entrada = models.CharField(max_length=20)
    Postre = models.CharField(max_length=20)
    Plato_Fuerte = models.CharField(max_length=20)
    Bebida = models.CharField(max_length=20)

    def _str_(self):
        return self.Entrada
    


class Administrador(models.Model):
    nombre_admin = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
 
    def _str_(self):
        return self.nombre_admin
    


class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    Categorias = models.ForeignKey('Categorias', on_delete=models.CASCADE)

 
    def _str_(self):
        return self.nombre
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def _str_(self):
        return self.nombre

class Orden(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=20)
    Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def _str_(self):
        return f'{self.fecha} - {self.Usuario}'

class Detalles_orden(models.Model):
    Orden = models.ForeignKey('Orden', on_delete=models.CASCADE)
    Menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()

    def _str_(self):
        return f'{self.fecha} - {self.Menu} - {self.Usuario}'