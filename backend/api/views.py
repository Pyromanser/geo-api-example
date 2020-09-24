from rest_framework import viewsets

from geo_data.models import GeoData
from geo_data.serializers import GeoDataModelSerializer


class GeoDataViewSet(viewsets.ModelViewSet):
    queryset = GeoData.objects.all()
    serializer_class = GeoDataModelSerializer
