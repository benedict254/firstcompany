from django.shortcuts import render
from .models import Product


def home(request):
    prod = Product.objects.all()
    return render(request,'web1/home.html',{'prod':prod})
