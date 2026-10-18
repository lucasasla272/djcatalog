from django.db import models


class DJ(models.Model):
    nombre = models.CharField(max_length=100)        # nombre artístico
    estilo = models.CharField(max_length=50)         # house, techno, trance, DnB...
    nacionalidad = models.CharField(max_length=50)
    debut_year = models.IntegerField()               # año en que empezo
    descripcion = models.TextField(blank=True)       # opcional

    class Meta:
        ordering = ['nombre']                        # orden por defecto alfabético

    def __str__(self):
        return f"{self.nombre} ({self.estilo})"