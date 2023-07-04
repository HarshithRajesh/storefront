from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(20,30))
    return render(request,"hello.html",{'name':'Ha','products':list(queryset)})
#random
