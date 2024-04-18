from tkinter import image_names
from turtle import mode
from django.db import models

# Create your models here.


class Empresa(models.Model):
    clave = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=100, null=True, blank=True)
    numero_interior = models.CharField(max_length=100, null=True, blank=True)
    colonia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
        managed= True
        db_table = 'empresa'

    def __str__(self):
        return self.razon_social
    
class Sucursal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=100, null=True, blank=True)
    numero_interior = models.CharField(max_length=100, null=True, blank=True)
    colonia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'
        managed= True
        db_table = 'sucursal'

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    clave = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        managed= True
        db_table = 'producto'

    def __str__(self):
        return self.descripcion
        
class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'imagenes'
        managed= True
        db_table = 'imagen'

    def __str__(self):
        return self.imagen