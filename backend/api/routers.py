from django.urls import path, include
from rest_framework import routers

from api.views import GeoDataViewSet

router = routers.DefaultRouter()
router.register(r'geo', GeoDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
