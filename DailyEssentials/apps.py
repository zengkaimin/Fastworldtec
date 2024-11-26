from django.apps import AppConfig  # Import the AppConfig class from django.apps


# Define a configuration class for the daily essentials application
class DailyEssentialsConfig(AppConfig):
    # Specify the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the application
    name = 'DailyEssentials'
    verbose_name = 'Daily Essentials Management'
