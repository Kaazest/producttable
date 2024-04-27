from django.db import models

# Create your models here.
class Products(models.Model):
    esGratuito = models.BooleanField(default=False)

    fecha_hora = models.DateTimeField(auto_now_add=True)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.IntegerField()

    nombre_producto = models.TextField(max_length=100)
    
