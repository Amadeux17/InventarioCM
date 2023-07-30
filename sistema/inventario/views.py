from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, "index.html")

def productos(request):
    return render(request, "productos/index.html")

def categorias(request):
    return render(request, "categorias/index.html")