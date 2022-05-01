# Create your views here.
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Item


def home(req):
    data = {'page_title': "Docs App",
            'greet': "Welcome to Home Page"}
    return render(req, 'itemCatalog/home.html', context=data)


def item_list(req):
    data = {'page_title': "Docs App",
            'greet': "Welcome to Home Page"}
    return render(req, 'itemCatalog/item_list.html', context=data)


class MyListItemsView(View):
    template_name = 'itemCatalog/item_list.html'

    def get(self, req, *args, **kwargs):
        res = Item.objects.all()
        data = {'page_title': "List Items page",
                'greet': "list Items",
                'object_list': res,
                }
        return render(req, self.template_name, context=data)


class MyItemDetail(DetailView):
    model = Item


class MyListItems(ListView):
    model = Item


class MyItemDetailView(View):
    model = Item
    template_name = 'itemCatalog/item_detail.html'

    def get(self, req, *args, **kwargs):
        my_item = get_object_or_404(Item, id=kwargs['id'])
        return render(req, self.template_name, {'i': my_item})
