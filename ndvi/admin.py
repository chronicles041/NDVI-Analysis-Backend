from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

# Customize the AdminSite class
admin.site.site_title = "NDVI Prediction Admin Portal"
admin.site.site_header = "NDVI Prediction Admin"
admin.site.index_title = "Welcome to NDVI Prediction Administration"

admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(WeatherData)
admin.site.register(NDVIAnalysis)

