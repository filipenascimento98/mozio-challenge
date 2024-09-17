from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from api.serializers.user_serializer import UsuarioSerializer


class UserView(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()
