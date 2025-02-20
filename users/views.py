from rest_framework import generics

from users.serializers import UserSerializer


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
