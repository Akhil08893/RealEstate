from .serializers import ListingSerializer
from RealEstate.models import *
from rest_framework import generics


class ListingView(generics.ListAPIView):
    queryset = Listings.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer
    
    
class ListingCreate(generics.CreateAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer
    
    
class ListingDetail(generics.RetrieveAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer
    
class ListingDelete(generics.DestroyAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer
    
class ListingUpdate(generics.UpdateAPIView):
    queryset = Listings.objects.all()
    serializer_class = ListingSerializer
