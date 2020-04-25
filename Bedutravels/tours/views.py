from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    return render(request,"tours/index.html")

"request contiene todos los datos de la peticion"""