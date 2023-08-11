from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages #import messages
from .forms import ProductUpdateForm,BrandUpdateForm,CategoryUpdateForm

from ecommerce.apps.catalogue.models import Product,Category,Brand,ProductImage
from ecommerce.apps.account.models import Customer

# Create your views here.

def home(request):
    return render(request,'custom_admin/homepage.html')

# ----------------------Product CRUD---------------------------#

def ProductListView(request):
    products = Product.objects.all()
    return render(request,'custom_admin/product_list.html',{'products':products})

def ProductAddView(request):
    categories =Category.objects.all()
    brands =Brand.objects.all()
    if request.method=="POST":

        data = request.POST
        print(data)
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
        return redirect('custom_admin:product_list')
    context = {
            "categories":categories,
            "brands":brands
        }
    return render(request,'custom_admin/product_add.html',context) 


def ProductUpdateView(request,pk):                                         
    data = get_object_or_404(Product, pk=pk)
    form = ProductUpdateForm(instance=data)
    if request.method == "POST":
        form =  ProductUpdateForm(request.POST, instance=data)
        #form2 =  UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,f'The Product Record Has Been Successfully Updated!')
            return redirect ('custom_admin:product_list')
    else:
        form = ProductUpdateForm(instance=data)
        messages.warning(request, 'Please correct the error below.')    

    context = {
        "form":form 
    }
    return render(request, 'custom_admin/product_update.html', context)

def ProductDeleteView(request,pk):                                         
    product = Product.objects.get(pk=pk)
    product.delete()
    products = Product.objects.all()
    # return redirect('custom_admin:product_list',{'products':products})
    return render(request,'custom_admin/partials/products_list.html',{'products':products})


# ----------------------Brand CRUD---------------------------#

def BrandListView(request):
    brands = Brand.objects.all()
    return render(request,'custom_admin/brand_list.html',{'brands':brands})

def BrandAddView(request):
    if request.method=="POST":
        name = request.POST.get('name')
        image = request.FILES['image']
        slug = request.POST.get('slug')
        is_active = request.POST.get('is_active')
        if is_active=="on":
            is_active = True
        else:
            is_active = False

        newBrand= Brand.objects.create(name=name,image=image,
                                       slug =slug,is_active=is_active)
        newBrand.save()
        messages.success(request, "New Brand Added Successfully" )
        return redirect('custom_admin:brand_list')
    return render(request,'custom_admin/brand_add.html') 


def BrandUpdateView(request,pk):                                         
    data = get_object_or_404(Brand, pk=pk)
    form = BrandUpdateForm(instance=data)
    if request.method == "POST":
        form =  BrandUpdateForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,f'The Brand Record Has Been Successfully Updated!')
            return redirect ('custom_admin:brand_list')
    else:
        form = BrandUpdateForm(instance=data)
        messages.warning(request, 'Please correct the error below.')    

    context = {
        "form":form 
    }
    return render(request, 'custom_admin/brand_update.html', context)

def BrandDeleteView(request,pk):                                         
    brand = Brand.objects.get(pk=pk)
    brand.delete()
    brands = Brand.objects.all()
    # return redirect('custom_admin:product_list',{'products':products})
    return render(request,'custom_admin/partials/brands_list.html',{'brands':brands})


# ----------------------Category CRUD---------------------------#

def CategoryListView(request):
    categories = Category.objects.all()
    return render(request,'custom_admin/category_list.html',{'categories':categories})

def CategoryAddView(request):                                         
    form = CategoryUpdateForm()
    if request.method == "POST":
        form =  CategoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'The Category Record Has Been Successfully Added!')
            return redirect ('custom_admin:category_list')
    else:
        form = CategoryUpdateForm()
        messages.warning(request, 'Please correct the error below.')    

    context = {
        "form":form 
    }
    return render(request, 'custom_admin/category_add.html', context)

def CategoryUpdateView(request,pk):                                         
    data = get_object_or_404(Category, pk=pk)
    form = CategoryUpdateForm(instance=data)
    if request.method == "POST":
        form =  CategoryUpdateForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,f'The Category Record Has Been Successfully Updated!')
            return redirect ('custom_admin:category_list')
    else:
        form = CategoryUpdateForm(instance=data)
        messages.warning(request, 'Please correct the error below.')    

    context = {
        "form":form 
    }
    return render(request, 'custom_admin/category_update.html', context)

def CategoryDeleteView(request,pk):                                         
    category = Category.objects.get(pk=pk)
    category.delete()
    categories = Category.objects.all()
    return render(request,'custom_admin/partials/categories_list.html',{'categories':categories}) 


# ----------------------Order CRUD---------------------------#

def order_list(request):
    return render(request,'custom_admin/order_list.html')


# ----------------------Customer CRUD---------------------------#
def CustomerListView(request):
    customers = Customer.objects.all()
    return render(request,'custom_admin/customer_list.html',{'customers':customers})