from rest_framework import serializers
from users.models import *
from RealEstate.models import Listings
from RealEstate.api.serializers import ListingSerializer

class ProfileSerializer(serializers.ModelSerializer):
    seller_listings = serializers.SerializerMethodField()
    
    def get_seller_listings(self,obj):
        query =  Listings.objects.filter(seller = obj.seller)
        listings_serializer = ListingSerializer(query,many = True)    
        return listings_serializer.data
        
    class Meta:
        model = Profile
        fields = '__all__'