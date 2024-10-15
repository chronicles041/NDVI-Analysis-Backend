from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Farm, Crop, NDVIAnalysis, WeatherData

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['id', 'name', 'growing_season', 'ideal_ndvi_range']

class FarmSerializer(serializers.ModelSerializer):
    crop = CropSerializer(read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Farm
        fields = ['id', 'name', 'location', 'size', 'crop', 'soil_type', 'irrigation_type', 'user']

class NDVIAnalysisSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(read_only=True)

    class Meta:
        model = NDVIAnalysis
        fields = ['id', 'farm', 'ndvi_value', 'analysis_date']

class WeatherDataSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(read_only=True)

    class Meta:
        model = WeatherData
        fields = ['id', 'farm', 'temperature', 'humidity', 'precipitation', 'recorded_at']
