from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Modulos(models.Model):
    codigo = models.CharField(max_length=15, verbose_name='Modulos')
    description = models.TextField(blank=True, verbose_name='Descripción')
    estado = models.BooleanField(default=True, verbose_name='Estado')

class Personas(models.Model):
    cedula = models.CharField(max_length=13, verbose_name='Cedula/Ruc')
    nombres = models.CharField(max_length=60, verbose_name='Nombres/Apellidos')
    direccion = models.CharField(max_length=60, verbose_name='Dirección')    
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha Creación')
    datecompleted = models.DateTimeField(null=True, verbose_name='Completado')
    estado = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.nombres

class Abonados(models.Model):
    modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    area_has = models.FloatField(default=0, verbose_name='Area Neta de Riego (Has)')
    area_mt = models.FloatField(default=0, verbose_name='Area Neta de Riego (M2)')
    valor_m = models.FloatField(default=0, verbose_name='Recaudación Modulo')
    valor_j = models.FloatField(default=0, verbose_name='Valor Junta Agua')
    escritura = models.BooleanField(default=False, verbose_name='Escritura')
    observacion = models.CharField(max_length=300, verbose_name='Observación')
    create_registro =models.DateTimeField(auto_now_add=True, verbose_name='Fecha Registro')
    estado = models.BooleanField(default=True, verbose_name='Activo/Inactivo')