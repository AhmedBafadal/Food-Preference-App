from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    # Name of Restaurant
    name = models.CharField(max_length=120)
    # Location of Restaurant
    location = models.CharField(max_length=120,null=True,blank=True)
    # Category of Restaurant
    category = models.CharField(max_length=120, null=True, blank=True)
    # Date post added to db
    timestamp = models.DateTimeField(auto_now_add=True,)
    # Date post updated
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
