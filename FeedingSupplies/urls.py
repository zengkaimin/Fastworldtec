from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the feeding supplies app
app_name = 'feeding_supplies'

# URL patterns for the feeding supplies app
urlpatterns = [
    # Define url to map the 'feeding_supplies_view' function in views.py
    path('', views.feeding_supplies_view, name='feeding_supplies'),
]
