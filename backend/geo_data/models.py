from django.contrib.gis.db import models


class GeoData(models.Model):
    location = models.PointField(geography=True)
    address = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"GeoData ({self.longitude} - {self.latitude})"

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y
