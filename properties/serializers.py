from django.db import models
from rest_framework import serializers
from .models import Properties,Bid, Youtube

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = "__all__"


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Youtube
        fields = "__all__"