from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<b>Mumbai Indians Cricket Team...One of the most high-profile team in the tournment(Mumbai Indians)</b>') 
