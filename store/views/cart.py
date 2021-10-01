from django.shortcuts import render , redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models.product import Product


print(make_password('1234'))

class Cart(View):
    def get(self , request): # Handel get request
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html' , {'products': products})




