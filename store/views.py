from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .models import Product

from .forms import RegistrationForm
from django.contrib.auth import login

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form' : form})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('product_list')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart_detail.html', {'cart':cart})