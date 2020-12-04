from . import views
from django.urls import path

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("inicio/", views.inicio, name='inicio'),
    path("sobre-nosotros/", views.sobre_nosotros, name='sobre-nosotros'),
    path("sobre-pagina/", views.sobre_la_página, name='sobre-pagina'),
    
]
