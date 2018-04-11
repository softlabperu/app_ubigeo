from django.db import models


class Departamento(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField(blank=False, null=False, max_length=250, unique=True)


class Provincia(models.Model):
    class Meta:
        unique_together = ('nombre', 'departamento')

    def __str__(self):
        return self.nombre + " - " + self.departamento.nombre

    nombre = models.CharField(blank=False, null=False, max_length=250)
    departamento = models.ForeignKey(Departamento)


class Distrito(models.Model):
    class Meta:
        unique_together = ('nombre', 'provincia')

    def __str__(self):
        return self.nombre + " - " + self.provincia.nombre + " - " + self.provincia.departamento.nombre

    nombre = models.CharField(blank=False, null=False, max_length=250)
    ubigeo = models.CharField(blank=False, null=False, max_length=10)
    provincia = models.ForeignKey(Provincia)