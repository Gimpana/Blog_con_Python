from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

#Modelo de categorias

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")

    class Meta:
        ordering = ["created_at"]
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
    
    def __str__(self):
        return self.name
    

class Article(models.Model):

    title = models.CharField(max_length=50, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User,verbose_name="Usuario", editable=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True, related_name="articles")
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")
    update_at = models.DateField(auto_now=True, verbose_name="Editado el ")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.title
