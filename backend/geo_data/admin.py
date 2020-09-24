from django.contrib import admin
from geo_data.models import GeoData


@admin.register(GeoData)
class GeoDataModelAdmin(admin.ModelAdmin):
    list_display = ["address", "longitude", "latitude", "timestamp"]
    date_hierarchy = "timestamp"
