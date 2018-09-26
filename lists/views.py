from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home_page(request):
    new_item_text = request.POST.get('new_item_text', '')
    return render(request, 'home.html', {
        'new_item_text': new_item_text
    })
