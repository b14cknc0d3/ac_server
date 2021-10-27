
from django.urls import path
from properties.views import BidCreateView, PropertiesCreateView, PropertiesView


urlpatterns = [
    path("api/properties/",  PropertiesView.as_view(), name="properties_list"),
    path("api/bid/<int:pk>/", BidCreateView.as_view(), name="bid_create"),
    path("api/properties/create/", PropertiesCreateView.as_view(), name="properties_create")
]
