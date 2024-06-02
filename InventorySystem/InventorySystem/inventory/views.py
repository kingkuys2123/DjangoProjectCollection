from django.shortcuts import render, redirect
from .models import Supplier, Product


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})


def products_list(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    products = Product.objects.filter(supplier=supplier)

    return render(request, 'products.html', {'supplier': supplier, 'products': products})

def add_product(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)

    if request.method == 'POST':
        product_name = request.POST.get('name')
        product_code = request.POST.get('product_code')
        product_description = request.POST.get('description')
        product_brand = request.POST.get('brand')
        product_price = request.POST.get('price')
        product_quantity_available = request.POST.get('quantity_available')

        product = Product.objects.create(supplier=supplier, name=product_name, product_code=product_code, description=product_description, brand=product_brand, price=product_price, quantity_available=product_quantity_available)

        product.save()

    return redirect('products_list', supplier_id)
