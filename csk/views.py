from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>Ruturaj is captain of csk(chennai super kings)</h1>') 
    
