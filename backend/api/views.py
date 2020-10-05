from rest_framework import viewsets, mixins
from rest_framework import permissions

from geo_data.models import GeoData
from geo_data.serializers import GeoDataModelSerializer


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
