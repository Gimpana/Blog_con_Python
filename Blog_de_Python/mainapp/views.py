from django.shortcuts import render


# Create your views here.

def inicio(request):

    return render(request, 'index.html', {
        'title':'Inicio'
    })


def sobre_nosotros(request):

    return render(request, "sobre_nosotros.html", {
        'title': 'Sobre nosotros'
    })

def sobre_la_página(request):

    return render(request, 'sobre_la_pagina.html', {
        'title': 'Sobre la página'
    })