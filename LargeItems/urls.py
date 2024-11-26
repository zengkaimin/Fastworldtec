from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the large items app
app_name = 'large_items'

# URL patterns for the large items app
urlpatterns = [
    # Define URL to map the large_items_view function in views.py
    path('', views.large_items_view, name='large_items'),
]
