from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from api.serializers.provider_serializer import ProviderSerializer
from api.domain.provider_domain import ProviderDomain


class ProviderView(GenericViewSet, 
    mixins.CreateModelMixin, mixins.RetrieveModelMixin,
    mixins.ListModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin):

    domain = ProviderDomain()

    queryset = domain.list()['message']
    serializer_class = ProviderSerializer