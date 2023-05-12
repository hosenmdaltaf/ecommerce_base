from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages #import messages
from .forms import ProductUpdateForm

from ecommerce.apps.catalogue.models import Product,Category,Brand,ProductImage

# Create your views here.

def home(request):
    return render(request,'custom_admin/homepage.html')

def product_list(request):
    products = Product.objects.all()
    return render(request,'custom_admin/product_list.html',{'products':products})

def product_add(request):
    categories =Category.objects.all()
    brands =Brand.objects.all()
    if request.method=="POST":

        data = request.POST
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        else:
            category = None
        category = request.POST.get("category")

        title = request.POST.get('title')
        brand = request.POST.get('brand')
        unit = request.POST.get('unit')
        unit_choices = request.POST.get('unit_choices')
        description = request.POST.get('description')
        slug = request.POST.get('slug')
        stock = request.POST.get('stock') 
        regular_price = request.POST.get('regular_price') 
        discount_price = request.POST.get('discount_price')
        is_active = request.POST.get('is_active')
        if is_active=="on":
            is_active = True
        else:
            is_active = False

        newProduct=Product.objects.create(title=title,category_id=category,unit=unit,
                                      unit_choices=unit_choices,description=description,
                                       slug =slug,stock=stock,regular_price=regular_price,
                                     discount_price=discount_price,is_active=is_active,
                                      brand_id=brand )
        newProduct.save()

        messages.success(request, "Product Added Successfully" )

        # context = {
        #     "categories":categories,
        #     "brands":brands
        # }

        # messages.success(request,  'Your account has been successfully created')
        # return redirect('account:loginpage')
    return render(request,'custom_admin/add_product.html',{"categories":categories,"brands":brands}) 


def ProductUpdateView(request,pk):                                         
    data = get_object_or_404(Product, pk=pk)
    form = ProductUpdateForm(instance=data)
    print('--------test---') 
    print(form)

    if request.method == "POST":
        form =  ProductUpdateForm(request.POST, instance=data)
        #form2 =  UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,f'The Product Record Has Been Successfully Updated!')
            return redirect ('custom_admin:product_list')
    else:
        form = ProductUpdateForm(instance=data)
        #form2 = UpdateUserForm(instance=data.user)
        # form2 =  UpdateUserForm( instance=data.user)
        #form2 = UpdateUserForm(instance=request.user)
        # messages.warning(request, 'Please correct the error below.')    

    context = {
        "form":form 
    }
    return render(request, 'custom_admin/product_update.html', context)


def order_list(request):
    return render(request,'custom_admin/order_list.html')
