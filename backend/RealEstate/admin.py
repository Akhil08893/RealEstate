from django.contrib import admin
from .models import *
from .forms import *


class PoiAdmin(admin.ModelAdmin):
    form = PoisForm



admin.site.register(Listings)
admin.site.register(Poi,PoiAdmin)

