from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm
# Create your views here.

# This is to create a feed based on who the user logged in has followed 
class HomeView(View):
    def get(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "home.html", {})
        user = request.user
        # Obtaining user ids
        is_following_user_ids = [x.user_id for x in user.is_following.all()]#User profiles being followed
        # Obtaining items, based off of user ids
        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True).order_by('-updated')[:3]
        return render(request, "menus/home-feed.html", {'object_list':qs})


# Below views are for a user viewing and creating their own items
class ItemListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ItemForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    # Passing in keyword arguments to the form class (Need to make sure form class handles arguments)
    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Menu Item'
        return context

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'menus/detail-update.html'
    form_class = ItemForm

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Menu Item'
        return context