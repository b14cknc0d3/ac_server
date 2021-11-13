from django.db import models
from rest_framework import serializers
from .models import Properties,Bid, Youtube


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"
        

class BidPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ("bid_price",)
class PropertySerializer(serializers.ModelSerializer):
    bidders =BidPrivateSerializer(many=True, read_only=True)
    class Meta:
        model = Properties
        fields = ("id","name","price","phone","image","video_links","description","owner_or_broker","category","bidders")





class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Youtube
        fields = "__all__"