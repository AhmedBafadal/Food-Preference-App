from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.http import Http404
from restaurants.models import RestaurantLocation
from menus.models import Item
# Create your views here.
User = get_user_model()

# Note!! remember to make a template tag filter after the below endpoint!
class ProfileFollowToggle(View):
    def post(self, request, *args, **kwargs):
        print(request.data)
        print(request.POST)
        return redirect('/u/cfe/')



class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'
    # Obtaining the user object
    def get_object(self,):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
    
    def get_context_data(self,*args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # print(context)
        user = context['user']         #self.get_object()
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user)
        qs = RestaurantLocation.objects.filter(owner=user).search(query)  # Queryset based on owner
         
        if items_exists and qs.exists():
            context['locations'] = qs
    
        return context