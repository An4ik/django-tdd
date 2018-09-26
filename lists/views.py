from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Item


@csrf_protect
def home_page(request):
    new_item_text = request.POST.get('new_item_text', '')

    new_item = Item.objects.create(text=new_item_text)
    new_item.save()

    return render(request, 'home.html', {
        'new_item_text': new_item.text
    })
