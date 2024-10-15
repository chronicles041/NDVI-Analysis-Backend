from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Crop(models.Model):
    name = models.CharField(max_length=100)
    growing_season = models.CharField(max_length=100)  # Example: "Spring-Summer"
    ideal_ndvi_range = models.CharField(max_length=50)  # Example: "0.5 - 0.8"

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    size = models.FloatField(default=0.0, help_text="Farm size in hectares")
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, related_name='farms')
    soil_type = models.CharField(max_length=100, blank=True)
    irrigation_type = models.CharField(max_length=100, blank=True, choices=(
        ('Drip', 'Drip'),
        ('Sprinkler', 'Sprinkler'),
        ('Flood', 'Flood'),
    ))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farms')

    def __str__(self):
        return f'{self.name} ({self.location})'

class NDVIAnalysis(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='ndvi_readings')
    ndvi_value = models.FloatField()
    analysis_date = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = "NDVI Analysis"
        verbose_name_plural = "NDVI Analysis"  # Correct plural

    def __str__(self):
        return f'NDVI Analysis for {self.farm.name} on {self.analysis_date.strftime("%Y-%m-%d")}'

class WeatherData(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='weather_data')
    temperature = models.FloatField(help_text="Temperature in Celsius")
    humidity = models.FloatField(help_text="Humidity percentage")
    precipitation = models.FloatField(help_text="Precipitation in mm")
    recorded_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Weather Data"
        verbose_name_plural = "Weather Data"  # Explicit pluralization

    def __str__(self):
        return f'Weather Data for {self.farm.name} on {self.recorded_at.strftime("%Y-%m-%d")}'