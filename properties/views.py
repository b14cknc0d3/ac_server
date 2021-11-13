from django.db import models
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView,CreateAPIView
from properties.models import Bid, Properties, Youtube

from properties.serializers import BidSerializer, PropertySerializer

# Create your views here.

class PropertiesView(ListAPIView):
    permission_class =()
    serializer_class=PropertySerializer
    queryset = Properties.objects.all()


class BidCreateView(CreateAPIView):
    permission_class=()
    serializer_class=BidSerializer
    queryset = Bid.objects.all()


class PropertiesCreateView(CreateAPIView):
    permission_class=()
    serializer_class = PropertySerializer
    queryset = Properties.objects.all()
    
    
    
class YouTubeView(ListAPIView):
    permission_class=()
    queryset=Youtube.objects.all()