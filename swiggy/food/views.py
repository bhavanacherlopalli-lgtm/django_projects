from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def biriyani(request):
    return HttpResponse('saturday no biryani')


def pizza(request):
    return HttpResponse('i do not like pizza')
