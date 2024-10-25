from django.db import models

# Create your models here.
class Categoria(models.Model):
    Nombre_Categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"nombre: {self.Nombre_Categoria}"  