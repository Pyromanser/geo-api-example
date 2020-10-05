from django.urls import path, include
from rest_framework import routers

from api.views import GeoDataViewSet, AddressToGeocodeView, GeocodeToAddressView

router = routers.DefaultRouter()
router.register(r'geo', GeoDataViewSet)


urlpatterns = [
    path("geo/address-to-geocode/", AddressToGeocodeView.as_view(), name="address-to-geocode"),
    path("geo/geocode-to-address/", GeocodeToAddressView.as_view(), name="geocode-to-address"),
    path('', include(router.urls)),
]
