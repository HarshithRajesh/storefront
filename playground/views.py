from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

def say_hello(request):

    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass
    return render(request,"hello.html")
