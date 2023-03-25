from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'custom_admin/homepage.html')

def product_add(request):
    return render(request,'custom_admin/add_product.html')

def product_list(request):
    return render(request,'custom_admin/product_list.html')

def order_list(request):
    return render(request,'custom_admin/order_list.html')
