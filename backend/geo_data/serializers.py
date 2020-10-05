from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from geo_data.models import GeoData


class GeoDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = ["location", "address"]


class GEOReadOnlySerializer(serializers.Serializer):
    address = serializers.CharField(read_only=True)
    latlng = gis_serializers.GeometryField(read_only=True)


class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(required=True)
    latlng = gis_serializers.GeometryField(read_only=True)


class LatLngSerializer(serializers.Serializer):
    address = serializers.CharField(read_only=True)
    latlng = gis_serializers.GeometryField(required=True)
