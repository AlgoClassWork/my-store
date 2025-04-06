from django.shortcuts import render

from store.models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

