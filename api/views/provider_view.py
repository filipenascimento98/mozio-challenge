from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api.serializers.provider_serializer import ProviderSerializer
from api.models import Provider


class ProviderView(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
