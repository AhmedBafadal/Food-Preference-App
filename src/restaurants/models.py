from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_category
# Create your models here.
class RestaurantLocation(models.Model):
    # Name of Restaurant
    name = models.CharField(max_length=120)
    # Location of Restaurant
    location = models.CharField(max_length=120,null=True,blank=True)
    # Category of Restaurant
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category,])
    # Date post added to db
    timestamp = models.DateTimeField(auto_now_add=True,)
    # Date post updated
    updated = models.DateTimeField(auto_now=True)
    # Slug field
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save_reciever(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



# def rl_post_save_reciever(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     # Below used to prevent recursion error (looping endlessly)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(rl_pre_save_reciever, sender=RestaurantLocation)

# post_save.connect(rl_post_save_reciever, sender=RestaurantLocation)
