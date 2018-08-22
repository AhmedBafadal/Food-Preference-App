from django.conf.urls import url

from .views import ProfileDetailView, RandomProfileDetailView

urlpatterns = [
    # Random user profile
    url(r'^random/$', RandomProfileDetailView.as_view(), name='random'),
#     # Lookups based on the username
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]