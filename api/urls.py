from django.urls import path, include
from rest_framework import routers
from api.views.provider_view import ProviderView
from api.views.service_area_view import ServiceAreaView, ServiceAreaAvaiableView
from api.views.user_view import UserView


router = routers.DefaultRouter()
router.register(r'provider', ProviderView, basename='provider')
router.register(r'service-area', ServiceAreaView, basename='service-area')
router.register(r'user', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('service-area-avaiable/', ServiceAreaAvaiableView.as_view(), name='service-area-avaiable')
]
