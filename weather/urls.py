from django.urls import path

from weather import views

urlpatterns = [
    path('', views.GetWeatherAPIView.as_view(), name='index'),  # для получения прогноза погоды
    path('add/', views.AddWeatherAPIView.as_view(), name='add-weather')  # для добавления города
]
