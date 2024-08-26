from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index</h1>")

def vista1(request):
    return HttpResponse("<h1<Soy la vista</h1>")