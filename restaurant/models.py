from re import M
from django.db import models

# Create your models here.
class Plato(models.Model):
    nombre =models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre