from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "inventory/home.html")

def product_list(request):
    products_in_stock = Product.objects.filter(in_stock=True)
    products_out_stock = Product.objects.filter(in_stock=False)
    return render(request, "inventory/product_list.html", {
        "products_in_stock": products_in_stock,
        "products_out_stock": products_out_stock,
    })
