from django.apps import AppConfig  # Import the AppConfig class from django.apps


# Configuration class for the sleep essentials app
class SleepEssentialsConfig(AppConfig):
    # Set the default auto field type to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # Define the name of the app
    name = 'SleepEssentials'
    verbose_name = 'Sleep Essentials Management'
