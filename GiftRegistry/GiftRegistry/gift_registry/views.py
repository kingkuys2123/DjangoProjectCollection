from django.shortcuts import render, redirect
from .models import Gift

def gift_list(request):
    gifts = Gift.objects.all()
    return render(request, 'gift_list.html', {'gifts': gifts})


def gift_detail(request, pk):
    gift = Gift.objects.get(pk=pk)

    if request.method == 'POST':
        gift.purchased = True
        gift.save()
        return redirect('gift_detail', pk=pk)

    return render(request, 'gift_detail.html', {'gift': gift})