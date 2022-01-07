from django.urls import path
from . import views

urlpatterns = [
    path("",views.hola,name="primer saludo"),
    #path("<str:varNombre>/",views.saludo ,name="saludo a todos"),
    path("moneda/",views.moneda,name="moneda")
]
