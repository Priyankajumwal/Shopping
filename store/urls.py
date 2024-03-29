from django.urls import path
from .views.home import Index #, order
from .views.signup import Signup
from .views.login import Login , logout
from django.contrib import admin
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import Orderview
from .middlewares.auth import auth_middleware



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', auth_middleware(CheckOut.as_view()), name='checkout'),
    path('orders', auth_middleware(Orderview.as_view()), name='orders'),
]
