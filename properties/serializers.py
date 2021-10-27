from django.db import models
from rest_framework import serializers
from .models import Properties,Bid

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = "__all__"


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"


