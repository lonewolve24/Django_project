from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ItemForm
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
    
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('phone:index')
    
    context = {
        "form":form,
    }
    return render(request, 'phone/item-form.html', context)


def update_item(request, id):

       item = Item.objects.get(id=id)
       form  = ItemForm(request.POST or None, instance=item)

       if form.is_valid():
            form.save()
            return redirect('phone:index')
       
       context = {
            
            'form':form,
            'item':item,
       }
       
       return render( request, 'phone/item-form.html', context)

def delete_item(request, id):
     item = Item.objects.get(id=id)
     
     if request.method == 'POST' :
          
          item.delete()
          return redirect('phone:index')
     context = {
          
          'item': item
     }

     return render( request, 'phone/item-delete.html', context)