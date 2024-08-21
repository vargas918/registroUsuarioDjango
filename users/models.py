from django.db import models

# Create your models here.


class Persona(models.Model):
    ESTADO_CHOICES =[
        ('activo', 'Activo'),
        ('inactivo','Inactivo')
    ]

    name= models.CharField(max_length=100)
    cedula=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    estado=models.CharField(max_length=100,
    choices= ESTADO_CHOICES, default='activo')
    dateCreated=models.DateField(auto_now=True)