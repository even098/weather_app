from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User
from weather.models import Weather


class TestGetWeatherAPIView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = 'http://127.0.0.1:8000/api/weather/'
        self.location = self.location = Weather.objects.create(location='London', country='UK', temperature=5,
                                                               feelslike=20, wind_speed=10,
                                                               humidity=0, visibility=0)
        self.user = User.objects.create_user(username='test', password='test', role='user', location=self.location)

    def test_get_weather(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['location'], self.location.location)
