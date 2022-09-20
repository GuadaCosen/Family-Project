from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime



def saludo(request):

    nombre = "Guada"

    nacionalidad = "Argentina"

    horaActual = datetime.now()

    intereses = ["Programar", "Ver series", "Ir al gimnasio"]
    
    diccionario = {"name":nombre, "country":nacionalidad, "hora":horaActual, "intereses":intereses,}

    miHtml = open("C:/Users/tlrte/OneDrive/One Drive/OneDrive/Desktop/ProyectosCoder/Proyecto1/Proyecto1/plantillas/saludar.html")
    
    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    #plantilla = loader.get_template("saludar.html")

    #documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def sumar(request):
    return HttpResponse("En esta pagina voy a sumar numeros ")

def miNombre(self, nombre):
    texto = f"Mi nombre es: " , nombre
    return HttpResponse(texto)

def calcular(request):
    tiempoActual = datetime.now()

    miCumple = datetime(2023,1,3)

    tiempoFalta = miCumple-tiempoActual

    resultadoMinutos = tiempoFalta.days *60*24 + tiempoFalta.seconds//60

    return HttpResponse(resultadoMinutos)


def probandoTemplate(self):

    miHtml = open ("C:/Users/tlrte/OneDrive/One Drive/OneDrive/Desktop/ProyectosCoder/Proyecto1/Proyecto1/plantillas/template.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
