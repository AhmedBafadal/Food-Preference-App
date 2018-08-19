from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from restaurants.models import RestaurantLocation
# Create your models here.

User = settings.AUTH_USER_MODEL

class Item(models.Model):
    # Associations
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(RestaurantLocation)
    # Menu item name
    name = models.CharField(max_length=120)
    # Menu ingredients
    contents = models.TextField(help_text='Please seperate each ingredient by comma.')
    # Menu ingredients to exclude
    excludes = models.TextField(blank=True, null=True, help_text='Please seperate each ingredient by comma.')
    # Allowing user to set menu to be visible by others or private
    public = models.BooleanField(default=True)
    # Time
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


    def get_absolute_url(self): #get_absolute_url
    #return f"/restaurants/{self.slug}" 
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        # Ordered by most recent
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(',')


    def get_excludes(self):
        return self.excludes.split(',')