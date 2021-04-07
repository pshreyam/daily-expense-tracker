from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from django.http import HttpResponse

from tracker.models import Item, Purchase

# def home(request):
#     return render(request, 'tracker/home.html')

def about(request):
    return render(request, 'tracker/about.html', {'title': 'About'})


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'tracker/home.html'
    context_object_name = 'purchases'
    ordering = ['-date_purchased']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Purchase.total()
        return context


class PurchaseDetailView(DetailView):
    model = Purchase
    context_object_name = 'purchase'


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = ['item', 'quantity', 'date_purchased']


class PurchaseUpdateView(UpdateView):
    model = Purchase
    fields = ['item', 'quantity', 'date_purchased']


class PurchaseDeleteView(DeleteView):
    model = Purchase
    success_url = '/'


class ItemListView(ListView):
    model = Item
    template_name = 'tracker/items.html'
    context_object_name = 'items'
    ordering = ['price']


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'price', 'description','img']


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'price', 'description','img']


class ItemDeleteView(DeleteView):
    model = Item
    success_url = '/items/'