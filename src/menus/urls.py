from django.conf.urls import url


from .views import (
    # restaurant_createview,
    # restaurant_listview,
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView

)
urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create/$',  ItemCreateView.as_view(), name='create'),
    # url(r'^update/(?P<pk>[\d-]+)/$',  ItemUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[\d-]+)/$', ItemDetailView.as_view(), name='detail'),
]