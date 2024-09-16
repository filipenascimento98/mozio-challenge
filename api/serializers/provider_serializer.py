from rest_framework.serializers import ModelSerializer
from api.models import Provider


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'