from django.db import models
from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    # Importante: ForeignKey apunta a Categoria (definida justo arriba)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='fotos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo