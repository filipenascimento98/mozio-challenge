from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from api.serializers.service_area_serializer import ServiceAreaSerializer
from api.domain.service_area_domain import ServiceAreaDomain


class ServiceAreaView(GenericViewSet, 
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
    mixins.ListModelMixin, mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin):

    domain = ServiceAreaDomain()
    
    queryset = domain.list()['message']
    serializer_class = ServiceAreaSerializer