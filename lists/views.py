from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Item


@csrf_protect
def home_page(request):
    new_item_text = request.POST.get('new_item_text', '')

    if request.method == 'POST' and new_item_text:
        new_item = Item.objects.create(text=new_item_text)
        new_item.save()
        return redirect('/')

    return render(request, 'home.html')
