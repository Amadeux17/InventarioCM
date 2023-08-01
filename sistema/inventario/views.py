from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def productos(request):
    return render(request, "productos/index.html")

def categorias(request):
    return render(request, "categorias/index.html")

def usuarios(request):
    return render(request, "usuarios/usuarios.html")

def roles(request):
    return render(request, "roles/roles.html")

def list_users(_request):
    users=list(usuario.objects.values())
    data={'usuario':users}
    return JsonResponse(data)