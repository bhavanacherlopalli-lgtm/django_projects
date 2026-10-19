

# Create your views here.
from django.http import HttpResponse

def wish(request, name):
    return HttpResponse("HELLO! HOW ARE YOU " + name)