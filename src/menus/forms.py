from django import forms
from .models import Item
from restaurants.models import RestaurantLocation
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    # Handling the arguments being passed into the form class from views.py
    def __init__(self, user=None, *args, **kwargs): # Instead of user=None, could also use - kwargs.pop('user')
        
        # Passing in a user to the item form
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user) # This allows each user creating a menu item to specifically select restaurants that they have posted.
