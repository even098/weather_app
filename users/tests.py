from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User
from weather.models import Weather


class TestRegistrationAPIView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = 'http://127.0.0.1:8000/api/users/registration/'
        self.location = Weather.objects.create(location='London', country='UK', temperature=5, feelslike=20, wind_speed=10,
                                               humidity=0, visibility=0)

    def test_registration_without_data(self):
        response = self.client.post(self.url, {'username': '', 'password': '', 'location_name': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_wrong_location(self):
        response = self.client.post(self.url, {'username': 'user1', 'password': 'user1', 'location_name': '-1'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_correct_data(self):
        response = self.client.post(self.url, {'username': 'user1', 'password': 'user1', 'location_name': 'London'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'user1')
        self.assertEqual(User.objects.count(), 1)
