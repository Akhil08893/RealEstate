"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from RealEstate.api import  views as listings_api_views
from users.api import views as user_api_views
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listing', listings_api_views.ListingView.as_view()),
    path('api/listing/create/', listings_api_views.ListingCreate.as_view()),
    path('api/listing/<int:pk>/', listings_api_views.ListingDetail.as_view()),
    path('api/listing/<int:pk>/delete/', listings_api_views.ListingDelete.as_view()),
    path('api/listing/<int:pk>/update/',listings_api_views.ListingUpdate.as_view()),
    
    
    path('api/profiles/',user_api_views.ProfileList.as_view()),
    path('api/profile/<int:seller>/', user_api_views.ProfileDetail.as_view()),
    path('api/profile/<int:seller>/update', user_api_views.ProfileUpdate.as_view()),
    
    
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
