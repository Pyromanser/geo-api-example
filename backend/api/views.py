import geocoder

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework import viewsets, generics, mixins, status
from rest_framework import permissions
from rest_framework.response import Response

from geo_data.models import GeoData
from geo_data.serializers import GeoDataModelSerializer, GEOReadOnlySerializer, AddressSerializer, LatLngSerializer


class GeoDataViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = GeoData.objects.all()
    serializer_class = GeoDataModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):

        return super(GeoDataViewSet, self).list(request, *args, **kwargs)


class AddressToGeocodeView(generics.GenericAPIView):
    serializer_class = AddressSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            geo = geocoder.google(serializer.data["address"])
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if not geo.latlng:
            return Response({"detail": "This address doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "latlng": geo.latlng,
                "address": geo.address,
            },
            status=status.HTTP_200_OK,
        )


class GeocodeToAddressView(generics.GenericAPIView):
    serializer_class = LatLngSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            geo = geocoder.google(serializer.data["latlng"]["coordinates"], method='reverse')
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if not geo.address:
            return Response({"detail": "This address doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "latlng": geo.latlng,
                "address": geo.address,
            },
            status=status.HTTP_200_OK,
        )
