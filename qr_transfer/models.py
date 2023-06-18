from django.db import models
from django.urls import reverse


class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.BinaryField()

    def es_imagen(self):
        return self.nombre.lower().endswith(
            (
            '.png', '.jpg', '.jpeg', '.gif' 
            )
        )
    
    def url_vista_previa(self):
        if self.es_imagen():
            return reverse('vista_previa_archivo', args=[self.id])
        else:
            return ''