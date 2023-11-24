from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def raju(request):
    return HttpResponse('<h1><marquee> hello world</h1></marquee>')
