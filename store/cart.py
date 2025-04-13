from decimal import Decimal
from .models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += 1

        self.session['cart'] = self.cart
        self.session.modified = True

    def get_total_price(self):
        return sum( Decimal(item['price']) * item['quantity'] for item in self.cart.values() )
    
    def __iter__(self):
        product_ids = self.cart.keys() 
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum( item['quantity'] for item in self.cart.values() ) 


