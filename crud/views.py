from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Arte

# Create your views here.
def index(request):
    lista_artes = Arte.objects.all()
    template = loader.get_template("index.html")
    context = {"artes":lista_artes}
    return HttpResponse(template.render(context,request))

def vista_detalle(request, id_arte):
    detalle_arte = Arte.objects.get(id = id_arte)
    template = loader.get_template("detail.html")
    context = {"arte":detalle_arte}
    return HttpResponse(template.render(context,request))