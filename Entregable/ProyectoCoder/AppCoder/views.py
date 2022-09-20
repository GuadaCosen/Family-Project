from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.


def curso(request):

    curso2 = Curso(nombre="Diseño", duracion=12345)

    curso2.save()

    return HttpResponse(f"Estoy guardando el primer curso. {curso2.nombre}")