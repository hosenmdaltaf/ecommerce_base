from django.urls import path

from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('product_add/', views.product_add, name='product_add'), 
    path('product_list/', views.product_list, name='product_list'), 
    path('update_product/<int:pk>', views.ProductUpdateView, name='update_product'), 
    
    path('order_list/', views.order_list, name='order_list'), 
]
