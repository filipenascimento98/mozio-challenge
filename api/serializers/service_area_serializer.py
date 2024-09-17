from django.contrib.gis.geos import Polygon
from rest_framework import serializers
from api.models import ServiceArea, Provider
from api.serializers.provider_serializer import ProviderSerializer, ProviderNameResponseSerializer


class ServiceAreaSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()

    def create(self, validated_data):
        provider_data = validated_data.pop("provider")
        provider = Provider.objects.create(**provider_data)

        coordinates = validated_data["coordinates"]
        validated_data["coordinates"] = Polygon([
            (coordinate['lng'], coordinate['lat'])
            for coordinate in coordinates]
        )
        return ServiceArea.objects.create(
            **validated_data, provider=provider
        )

    def update(self, instance, validated_data):
        try:
            provider_data = validated_data.pop("provider")
        except KeyError:
            provider_data = {}

        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        try:
            coordinates = validated_data.get("coordinates")
            instance.coordinates = Polygon([(coordinate['lng'], coordinate['lat']) for coordinate in coordinates])
        except Exception:
            # Lat and long invalid in update. Not update service area's coordinate
            pass
        instance.save()

        provider = instance.provider
        provider.email = provider_data.get('email', provider.email)
        provider.name = provider_data.get('name', provider.name)
        provider.phone_number = provider_data.get(
            'phone_number', provider.phone_number
        )
        provider.language = provider_data.get('language', provider.language)
        provider.currency = provider_data.get('currency', provider.currency)
        provider.save()

        return instance

    class Meta:
        model = ServiceArea
        fields = '__all__'
        extra_kwargs = {'coordinates': {'write_only': True}}


class ServiceAreaAvaiableRequestSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()


class ServiceAreaAvaiableResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
    provider = ProviderNameResponseSerializer()
    price = serializers.FloatField()
