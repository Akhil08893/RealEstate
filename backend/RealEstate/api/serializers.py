from RealEstate.models import *
from rest_framework import serializers
from django.contrib.gis.measure import D 
from django.contrib.gis.geos import Point


class ListingSerializer(serializers.ModelSerializer):
    seller_username = serializers.SerializerMethodField()
    agency_name = serializers.SerializerMethodField()
    listing_pois_within_10km =  serializers.SerializerMethodField()
    
    
    def get_listing_pois_within_10km(self,obj):
        listing_location = Point(obj.latitude,obj.longitude,srid=4326)
        query = Poi.objects.filter(location__distance_lte = (listing_location ,D(km=10)))
        query_serializer = PoiSerializer(query,many=True)
        return query_serializer.data
    
    
    def get_agency_name(self,obj):
        return obj.seller.profile.agency_name
    
    def get_seller_username(self,obj):
        return obj.seller.username
    
    class Meta:
        model = Listings
        fields = "__all__"
        
class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = "__all__"