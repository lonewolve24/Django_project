from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    items_list =Item.objects.all()
    context = { "items_list":items_list,}
    return render(request, 'phone/index.html', context)


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")

def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        "item": item,
    }
    return render(request, "phone/detail.html", context)
    
