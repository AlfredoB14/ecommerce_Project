from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def list_products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
