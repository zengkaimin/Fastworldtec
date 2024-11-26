from django.contrib import admin  # Import the admin module from Django
from .models import DailyEssentials  # Import the DailyEssentials model from the current app's models file
from .forms import DailyEssentialsForm  # Import the custom form class for DailyEssentials


# Define a custom admin class for the DailyEssentials model
class DailyEssentialsAdmin(admin.ModelAdmin):
    form = DailyEssentialsForm  # Specify the form to use in the admin interface


# Register the DailyEssentials model with the custom admin class
admin.site.register(DailyEssentials, DailyEssentialsAdmin)
