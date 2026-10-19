from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def chocolate(request):
    return HttpResponse('Eat fivestar do nothing')


def icecream(request):
    return HttpResponse('chocolate is better than the vanilla')
    



