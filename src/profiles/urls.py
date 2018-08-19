from django.conf.urls import url




from .views import (

    ProfileDetailView,
 
)

urlpatterns = [
    # Lookups based on the username
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),

]

