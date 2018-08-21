from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from restaurants.models import RestaurantLocation
from menus.models import Item
from .models import Profile
from .forms import RegisterForm
# Create your views here.
User = get_user_model()



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'
    
    # Override function
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('/logout')
        return super(RegisterView, self).dispatch(*args, **kwargs)



# Note!! remember to make a template tag filter after the ProfileFollowToggle endpoint!
class ProfileFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        username_to_toggle = request.POST.get('username')
        profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
        # print(is_following)
   

        return redirect(f'/u/{profile_.user.username}/')



class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'
    # Obtaining the user object
    def get_object(self,):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
    
    def get_context_data(self,*args, **kwargs):
        # Obtaining context data related to the specific user
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # print(context)
        user = context['user']         #self.get_object()
        # Following the user
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user).exists()
        qs = RestaurantLocation.objects.filter(owner=user).search(query)  # Queryset based on owner
         
        if items_exists and qs.exists():
            context['locations'] = qs
        return context