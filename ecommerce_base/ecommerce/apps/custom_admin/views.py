from django.http import HttpResponse
from django.shortcuts import render

from ecommerce.apps.catalogue.models import Product,Category,Brand,ProductImage

# Create your views here.

def home(request):
    return render(request,'custom_admin/homepage.html')

def product_add(request):
    categories =Category.objects.all()
    brands =Brand.objects.all()
    if request.method=="POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        unit = request.POST.get('unit')
        unit_choices = request.POST.get('unit_choices')
        description = request.POST.get('description')
        slug = request.POST.get('slug')
        stock = request.POST.get('stock')
        regular_price = request.POST.get('regular_price')
        discount_price = request.POST.get('discount_price')
        is_active = request.POST.get('is_active')

        newProduct=Product.objects.create(title=title,category=category,unit=unit,
                                      unit_choices=unit_choices,description=description,
                                       slug =slug,stock=stock,regular_price=regular_price,
                                     discount_price=discount_price,is_active=is_active,
                                      brand=brand )
        newProduct.save()

        # context = {
        #     "categories":categories,
        #     "brands":brands
        # }

        # messages.success(request,  'Your account has been successfully created')
        # return redirect('account:loginpage')
    return render(request,'custom_admin/add_product.html',{"categories":categories,"brands":brands}) 

def product_list(request):
    return render(request,'custom_admin/product_list.html')

def order_list(request):
    return render(request,'custom_admin/order_list.html')
