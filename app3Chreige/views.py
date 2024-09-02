from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Soy el index de Chreige</h1>")

def texto(request):
    html="<h1>Mondongo</h1>"
    return HttpResponse(html)