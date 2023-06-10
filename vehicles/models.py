from django.db import models

# Create your models here.
class Cars(models.Model):
    CATEGORY_CHOICES = [
        ("car", "Auto"),
        ("pickup", "Camioneta"),
        ("comercial", "Comercial"),
        ("suv", "SUV"),
        ("cross", "CrossOver"),
    ]
    brand = models.CharField(max_length=20, verbose_name="Marca",  default="Toyota") 
    model = models.CharField(max_length=35, verbose_name="Modelo" , null=True)    
    category = models.CharField(max_length=30, verbose_name="Categoria", choices=CATEGORY_CHOICES ,  default="car")
    img = models.ImageField(verbose_name="Imagen", upload_to="cars", null=True, blank=True)
    title= models.CharField(max_length=200 ,verbose_name="Titulo ", null=True, blank=True)
    description = models.TextField(verbose_name="Descripcion" ,null=False)
    year = models.IntegerField(verbose_name="Año" , null=False)
    price = models.IntegerField(verbose_name="Precio" ,null=False )

    class meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ["-created"]

    def __str__(self):
        return f"Marca: {self.brand} | Modelo: {self.model} | Año: {self.year} | Precio: ${self.price}"