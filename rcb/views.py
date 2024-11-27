from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1><marquee>ViratKohli is the captain of rcb(Royal challengers bengaluru)</marquee></h1>') 