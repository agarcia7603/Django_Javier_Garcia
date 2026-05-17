from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Nombre")
    last_name = models.CharField(max_length=200, verbose_name="Apellido")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    academic_title = models.CharField(max_length=200, verbose_name="Título académico")
    biography = models.TextField(null=True, blank=True, verbose_name="Biografía")
    email = models.EmailField(null=True, blank=True, verbose_name="Correo")
    dedication = models.CharField(max_length=200, verbose_name="Dedicatoria")
    image = models.ImageField(upload_to='profile', verbose_name="Imagen")
    occupation = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ocupación")


    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ["last_name"]
        db_table = "person"

    def __str__(self):
        return self.first_name + " " + self.last_name
