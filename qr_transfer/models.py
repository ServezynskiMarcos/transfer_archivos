from django.db import models

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.BinaryField()