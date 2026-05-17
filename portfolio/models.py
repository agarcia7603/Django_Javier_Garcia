from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='portfolio', null=True, blank=True, verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"
        ordering = ["-created"]
        db_table = "portfolio"

    def __str__(self):
        return self.title

