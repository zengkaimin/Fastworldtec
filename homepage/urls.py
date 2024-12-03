from django.urls import path  # Import the path function for defining URL patterns
from . import views  # Import the views module from the current package

# Define the app name for namespacing in URL patterns
app_name = 'homepage'

# URL patterns for the homepage app
urlpatterns = [
    # Define url to map the 'homepage_view' function in views.py
    path('', views.homepage_view, name='homepage'),

    # URL pattern for blog and review detail page
    path('blog/<slug:slug>/', views.blog_and_review_detail, name='blog_and_review_detail'),

    path('mark-completed/', views.mark_as_completed, name='mark_completed'),

]
