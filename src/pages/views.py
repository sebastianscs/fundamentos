import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, titulo, autor, fecha_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (Publicado el {self.fecha_publicacion}, ISBN: {self.isbn})"

# Crear un autor
autor1 = Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano")

# Crear un libro asociado al autor
libro1 = Libro(titulo="Cien años de soledad", autor=autor1, fecha_publicacion="1967-05-30", isbn="9780307474728")

# Crear otro autor y libro
autor2 = Autor(nombre="J.K. Rowling", nacionalidad="Británica")

libro2 = Libro(titulo="Harry Potter y la piedra filosofal", autor=autor2, fecha_publicacion="1997-06-26", isbn="9788478884456")

def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": "Autor: "+libro1.autor.nombre,
        "python_ver": "Libro: "+libro1.titulo,
    }

    return render(request, "pages/home.html", context)
