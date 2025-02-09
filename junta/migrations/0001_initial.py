# Generated by Django 5.1.4 on 2024-12-25 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, verbose_name='Modulos')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=13, verbose_name='Cedula/Ruc')),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombres/Apellidos')),
                ('direccion', models.CharField(max_length=60, verbose_name='Dirección')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha Creación')),
                ('datecompleted', models.DateTimeField(null=True, verbose_name='Completado')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
        migrations.CreateModel(
            name='Abonados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_has', models.FloatField(default=0, verbose_name='Area Neta de Riego (Has)')),
                ('area_mt', models.FloatField(default=0, verbose_name='Area Neta de Riego (M2)')),
                ('valor_m', models.FloatField(default=0, verbose_name='Recaudación Modulo')),
                ('valor_j', models.FloatField(default=0, verbose_name='Valor Junta Agua')),
                ('escritura', models.BooleanField(default=False, verbose_name='Escritura')),
                ('observacion', models.CharField(max_length=300, verbose_name='Observación')),
                ('create_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/Inactivo')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junta.modulos')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junta.personas')),
            ],
        ),
    ]
