from rest_framework import serializers

from geo_data.models import GeoData


class GeoDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = ["location", "address"]
