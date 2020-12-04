from . import views
from django.urls import path

urlpatterns = [
    path('articulos/', views.lista, name='lista-articulos')
]
