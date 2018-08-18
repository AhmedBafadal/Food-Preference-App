from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Item
# Create your views here.

class ItemListView(ListView):

    def get_queryset(self):
        return Item.objects.filter(user==self.request.user)