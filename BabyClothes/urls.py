from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the baby clothes app
app_name = 'baby_clothes'

# URL patterns for the courses app
urlpatterns = [
    # Define url to map the 'baby_clothes_view' function in views.py
    path('', views.baby_clothes_view, name='baby_clothes'),
]
