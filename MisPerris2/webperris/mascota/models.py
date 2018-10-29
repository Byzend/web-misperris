from django.db import models

# Create your models here.
class Mascota(models.Model):
    title = models.CharField(max_length=50 ,verbose_name ="Nombre")
    raza = models.CharField(max_length=50 ,verbose_name ="Raza")
    Estado = models.CharField(max_length=50 ,verbose_name ="Estado")
    description = models.TextField(verbose_name="Descripión")
    
    image = models.ImageField(verbose_name ="Foto", upload_to= "imgMascotas") 
    created = models.DateTimeField(auto_now_add=True ,verbose_name ="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha de edición")


    class Meta:
        ordering = ["-created"]


    def __str__(self):
        return self.title    