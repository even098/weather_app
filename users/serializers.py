from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import User
from weather.models import Weather

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(max_length=255, required=True, write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'location_name']

    def create(self, validated_data):
        location_name = validated_data.pop('location_name')
        location = Weather.objects.filter(location__iexact=location_name).first()
        # Берем location_name и получаем запись из таблицы Weather

        if location:
            user = UserModel.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                location=location
            )
            return user

        serialized_locations = LocationSerializer(Weather.objects.all(), many=True)
        raise serializers.ValidationError(
            {
                'detail': 'Something went wrong.',
                'available_locations': serialized_locations.data
            }
        )  # возвращаем список доступных городов из БД при неудачной регистрации


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ['location']
