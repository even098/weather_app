from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

from weather.models import Weather


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True
    )
    location = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, related_name='users')
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_manager(self):
        return self.role == 'manager'
    
    def __str__(self):
        return self.username
