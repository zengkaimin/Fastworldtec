from django.apps import AppConfig  # Import the AppConfig class from django.apps


# Define a configuration class for the large items application
class LargeItemsConfig(AppConfig):
    # Specify the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the application
    name = 'LargeItems'
    verbose_name = 'Large Items Management'
