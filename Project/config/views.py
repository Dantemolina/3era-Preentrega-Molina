from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def decoartesanal(request):
    productos = Producto.objects.filter(nombre__icontains='deco')
    return render(request, 'decoartesanal.html', {'productos': productos})

def decohogar(request):
    productos = Producto.objects.filter(nombre__icontains='deco')
    return render(request, 'decohogar.html', {'productos': productos})

def mates(request):
    productos = Producto.objects.filter(nombre__icontains='mate')
    return render(request, 'mates.html', {'productos': productos})

def organizadores(request):
    productos = Producto.objects.filter(nombre__icontains='organizadores')
    return render(request, 'organizadores.html', {'productos': productos})

def sobreMi(request):
    productos = Producto.objects.filter(nombre__icontains='sobreMi')
    return render(request, 'sobreMi.html', {'productos': productos})




