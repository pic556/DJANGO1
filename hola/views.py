from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def moneda(request):
    num =  1
    contex = {"numero":num}
    return render(request , "hola/moneda.html",contex)

def hola(request):
    return render(request,"hola/comienzo.html")

def saludo(request,varNombre):
    contex = {"name": varNombre }
    return render(request,"hola/saludo.html",contex)
