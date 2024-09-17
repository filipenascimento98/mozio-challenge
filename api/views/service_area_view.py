from django.contrib.gis.geos import Point
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from api.serializers.service_area_serializer import (
    ServiceAreaSerializer,
    ServiceAreaAvaiableRequestSerializer,
    ServiceAreaAvaiableResponseSerializer
)
from api.models import ServiceArea


class ServiceAreaView(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaAvaiableView(APIView):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    @swagger_auto_schema(query_serializer=ServiceAreaAvaiableRequestSerializer(),
                         responses={
                            200: ServiceAreaAvaiableResponseSerializer(many=True),
                            400: "Bad request.",
                            500: "Error querying the data in the database"
                        }
    )
    def get(self, request):
        serializer = ServiceAreaAvaiableRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        lng = serializer.data['lng']
        lat = serializer.data['lat']
        point = Point(lng, lat, srid=4326)

        services_avaiable = ServiceArea.objects.filter(
            coordinates__contains=point
        )

        serializer_response = ServiceAreaAvaiableResponseSerializer(data=services_avaiable, many=True)
        serializer_response.is_valid()

        return Response(data=serializer_response.data, status=status.HTTP_200_OK)
