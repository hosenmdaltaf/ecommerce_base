from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def index(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    categories = Category.objects.all().filter(is_active=True)[:12] 
    featured_product = Product.objects.prefetch_related("product_image").filter(is_feature=True)[:3]
    latest_products = Product.objects.prefetch_related("product_image").filter(is_active=True).order_by('-created_at')[:3]
    context ={
        "products": products, 
        "categories":categories,
        "featured_product":featured_product,
        "latest_products":latest_products
    }
    return render(request, "catalogue/homepage.html", context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "catalogue/single.html", {"product": product})

def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "catalogue/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "catalogue/category.html", {"category": category, "products": products})



