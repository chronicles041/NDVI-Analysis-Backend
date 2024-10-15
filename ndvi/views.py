from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Farm, Crop, NDVIAnalysis, WeatherData, User
from .serializers import FarmSerializer, CropSerializer, NDVIAnalysisSerializer, WeatherDataSerializer, UserSerializer

# Farm Viewset
class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.farms.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# NDVI Analysis Viewset
class NDVIAnalysisViewSet(viewsets.ModelViewSet):
    queryset = NDVIAnalysis.objects.all()
    serializer_class = NDVIAnalysisSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return NDVIAnalysis.objects.filter(farm__user=self.request.user)

# Weather Data Viewset
class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WeatherData.objects.filter(farm__user=self.request.user)

# Crop Viewset (for admins or public access)
class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAuthenticated]


# User Viewset (optional for listing users)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
