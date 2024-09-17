from rest_framework import serializers
from api.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderNameResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
