from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
