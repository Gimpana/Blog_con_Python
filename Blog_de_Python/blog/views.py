from django.shortcuts import render
from blog.models import Category, Article

# Create your views here.

def lista(request):

    articulo = Article.objects.all()
    
    return render(request, "articulos/lista.html", {
        'title': 'Articulos',
        'articulos': articulo
    })