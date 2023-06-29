from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x = 1
    y = 1
    return HttpResponse("Hello world")
