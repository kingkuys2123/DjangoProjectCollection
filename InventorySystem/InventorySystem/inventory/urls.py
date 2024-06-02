from django.urls import path
from .views import supplier_list, products_list, add_product

urlpatterns = [
    path('suppliers/', supplier_list, name='supplier_list'),
    path('products/<int:supplier_id>/', products_list, name='products_list'),
    path('products/add_product/<int:supplier_id>/', add_product, name='add_product'),
]