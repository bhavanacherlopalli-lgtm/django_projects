from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def friends(request):
    return HttpResponse('Indhu is my friend'),

def enemies(request):
    return HttpResponse('enemy')