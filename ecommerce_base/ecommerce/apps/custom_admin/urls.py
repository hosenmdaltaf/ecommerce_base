from django.urls import path

from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.home, name='admin_home'),

    # -----------------product CRUD-----------------#
    path('product_list/', views.ProductListView, name='product_list'),
    path('product_add/', views.ProductAddView, name='product_add'),  
    path('product_update/<int:pk>', views.ProductUpdateView, name='product_update'), 
    path('product_delete/<int:pk>', views.ProductDeleteView, name='product_delete'),  

    # -----------------brand CRUD-----------------#
    path('brand_list/', views.BrandListView, name='brand_list'),
    path('brand_add/', views.BrandAddView, name='brand_add'),
    path('brand_update/<int:pk>', views.BrandUpdateView, name='brand_update'),   
    path('brand_delete/<int:pk>', views.BrandDeleteView, name='brand_delete'), 

    # -----------------category CRUD-----------------#
    path('category_list/', views.CategoryListView, name='category_list'),
    path('category_add/', views.CategoryAddView, name='category_add'),
    path('category_update/<int:pk>', views.CategoryUpdateView, name='category_update'),   
    path('category_delete/<int:pk>', views.CategoryDeleteView, name='category_delete'), 
    
    # -----------------order CRUD-----------------#
    path('order_list/', views.order_list, name='order_list'), 
]
