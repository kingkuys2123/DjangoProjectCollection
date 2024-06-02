from django.shortcuts import render, redirect
from .models import WarehouseItem

# Create your views here.
def item_list(request):
    items = WarehouseItem.objects.all()
    return render(request, 'list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        item = WarehouseItem.objects.create(ItemName=name, Description=description, Quantity=quantity, Price=price)

        return redirect('item_list')

    return render(request, 'add.html')

def confirm_delete_item(request, item_id):
    item = WarehouseItem.objects.get(pk=item_id)
    return render(request, 'delete_item.html', {'item': item})

def delete_item(request, item_id):
    try:
        item = WarehouseItem.objects.get(pk=item_id)
        item.delete()
    except WarehouseItem.DoesNotExist:
        pass

    return redirect('item_list')

def edit_item(request, item_id):
    item = WarehouseItem.objects.get(pk=item_id)

    if request.method == 'POST':
        item.ItemName = request.POST.get('product_name')
        item.Description = request.POST.get('description')
        item.Quantity = request.POST.get('quantity')
        item.Price = request.POST.get('price')

        item.save()

        return redirect('item_list')

    return render(request, 'edit.html', {'item': item})