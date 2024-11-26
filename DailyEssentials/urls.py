from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the daily essentials app
app_name = 'daily_essentials'

# URL patterns for the daily essentials app
urlpatterns = [
    # Define url to map the daily_essentials_view function in views.py
    path('', views.daily_essentials_view, name='daily_essentials'),
]
