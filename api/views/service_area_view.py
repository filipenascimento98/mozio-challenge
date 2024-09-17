from django.contrib.gis.geos import Point
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api.serializers.service_area_serializer import (
    ServiceAreaSerializer, 
    ServiceAreaAvaiableSerializer
)
from api.models import ServiceArea


class ServiceAreaView(GenericViewSet, 
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
    mixins.ListModelMixin, mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

class ServiceAreaAvaiableView(APIView):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        serializer = ServiceAreaAvaiableSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        lng = serializer.data['lng']
        lat = serializer.data['lat']
        point = Point(lng, lat, srid=4326)

        services_avaiable = ServiceArea.objects.filter(
            coordinates__contains=point
        )

        services = []
        for service in services_avaiable:
            services.append(
                {
                    'name': service.name,
                    'provider_name': service.provider.name,
                    'price': service.price
                }
            )

        return Response(data=services, status=status.HTTP_200_OK)