from django.urls import path
from .views import home, products, exit, register

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('exit/', exit, name='exit'),
]
