from django.db import models


class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    temperature = models.DecimalField(max_digits=2, decimal_places=0)
    feelslike = models.DecimalField(max_digits=2, decimal_places=0)
    weather_descriptions = models.CharField(max_length=255, blank=False, null=False)
    wind_speed = models.DecimalField(max_digits=2, decimal_places=0)
    humidity = models.DecimalField(max_digits=2, decimal_places=0)
    visibility = models.DecimalField(max_digits=2, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('location', 'country')

    def __str__(self):
        return f'{self.location}, {self.country}'
