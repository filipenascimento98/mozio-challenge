from django.urls import path, include
from rest_framework import routers
from api.views.provider_view import ProviderView
from api.views.service_area_view import ServiceAreaView


router = routers.DefaultRouter()
router.register(r'provider', ProviderView, basename='provider')
router.register(r'service-area', ServiceAreaView, basename='service-area')

urlpatterns = [
    path('', include(router.urls)),
]