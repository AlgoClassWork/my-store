from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from .forms import RegistrationForm
from django.contrib.auth import login

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})