from django.urls import path  # Import path function for URL routing
from . import views  # Import views from the current app

# Define the application namespace for URL resolution
app_name = 'sleep_essentials'

urlpatterns = [
    # Define URL to map the 'sleep_essentials_view' function in views.py
    path('', views.sleep_essentials_view, name='sleep_essentials'),
]
