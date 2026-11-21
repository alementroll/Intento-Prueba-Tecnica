from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)