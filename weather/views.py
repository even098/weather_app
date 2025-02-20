from datetime import timedelta

import requests
from django.utils import timezone
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from weather.models import Weather
from weather.permissions import IsManager
from weather.serializers import WeatherSerializer
from weather_app.settings import API_KEY, BASE_URL


def get_and_update_weather_data(location):
    """Функция для обновления данных о погоде через отправки запроса на внешний API"""
    params = {
        'access_key': API_KEY,
        'query': location
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        location = data["location"]["name"]
        country = data["location"]["country"]

        weather, created = Weather.objects.update_or_create(
            location=location,
            country=country,
            defaults={
                "temperature": data["current"]["temperature"],
                "feelslike": data["current"]["feelslike"],
                "weather_descriptions": ", ".join(data["current"]["weather_descriptions"]),
                "wind_speed": data["current"]["wind_speed"],
                "humidity": data["current"]["humidity"],
                "visibility": data["current"]["visibility"],
                "updated_at": timezone.now(),
            }
        )

        return weather
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetWeatherAPIView(views.APIView):
    """View для получения данных о погоде по городу"""
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.location.updated_at >= timezone.now() - timedelta(minutes=10):
            weather_data = user.location  # если запись обновлена не больше 10 минут назад, берем её
        else:  # иначе обновляем запись через функцию и возвращаем данные
            weather_data = get_and_update_weather_data(user.location)
            serializer = WeatherSerializer(data=weather_data)

            if serializer.is_valid():
                serializer.save()

        weather_serialized_data = WeatherSerializer(weather_data).data

        return Response(data={'data': weather_serialized_data}, status=status.HTTP_200_OK)


class AddWeatherAPIView(views.APIView):
    """View для добавления городов в таблицу"""
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, *args, **kwargs):
        location = request.data.get('location')

        if Weather.objects.filter(location__iexact=location).exists():
            return Response({'detail': 'Location already exists.'}, status=status.HTTP_409_CONFLICT)

        weather_data = get_and_update_weather_data(location)
        weather_serialized_data = WeatherSerializer(weather_data).data

        return Response({'detail': 'Location successfully added.', 'Location weather': weather_serialized_data},
                        status=status.HTTP_200_OK)
