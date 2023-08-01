from django.db import models

# Create your models here.

class rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(null=True)

    class Meta:
        db_table: "rol"


class usuario(models.Model):
    iduser = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rolid = models.ForeignKey(rol, null=False,
                              blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table: "usuario"


class clasificacion(models.Model):
    idclasificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=True)
    ubicacion = models.CharField(max_length=20, null=True)

    class Meta:
        db_table: "clasificacion"


class producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    codigo = models.IntegerField(null=True)
    nombre = models.CharField(max_length=20, null=True)
    precio = models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    idclasificacion = models.ForeignKey(
        clasificacion, null=False, on_delete=models.CASCADE)
    iduser = models.ForeignKey(usuario, null=False, on_delete=models.CASCADE, default='')

    class Meta:
        db_table = "producto"