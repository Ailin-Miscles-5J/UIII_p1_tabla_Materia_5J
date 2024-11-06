from django.shortcuts import render
from .models import materia
# Create your views here.
def inicio_vista(request):
    lasmaterias=materia.objects.all()
    return render (request,"gestionarmnateria.html", {"mismaterias":lasmaterias})