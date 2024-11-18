from django.db import models

# Create your models here.
class Arte(models.Model):
    """
    Modelo que representa la estructura de
    datos de un trabajo de arte en base de
    datos
    """
    titulo = models.CharField(max_length=300)
    numero_referencia = models.CharField(max_length=40)
    fecha_pub = models.DateField()
    lugar_origen = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    imagen = models.FileField(upload_to="arte/")

    def __str__(self):
        return self.titulo