




# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def add_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')

        customer = Customer.objects.get(pk=customer_id)
        product = Product.objects.get(pk=product_id)

        total_price = product.price * int(quantity)

        order = Order.objects.create(customer=customer, product=product, quantity=quantity, total_price=total_price)

        return redirect('order_list')

    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'order_add.html', {'customers': customers, 'products': products})


def confirm_delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_confirm_delete.html', {'order': order})


def customer_orders(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)

    total_sales = sum(order.total_price for order in orders)

    return render(request, 'customer_orders.html', {'orders': orders, 'total_sales': total_sales})



def product_orders(request, product_id):
    orders = Order.objects.filter(product_id=product_id)

    total_sales = sum(order.total_price for order in orders)

    return render(request, 'product_orders.html', {'orders': orders, 'total_sales': total_sales})


def confirm_delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_confirm_delete.html', {'order': order})


def delete_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        order.delete()
        return redirect('order_list')
    except Order.DoesNotExist:
        return render(request, 'order_confirm_delete.html', {'error_message': 'Order does not exist.'})
