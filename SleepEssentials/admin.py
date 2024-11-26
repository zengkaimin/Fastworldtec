from django.contrib import admin  # Import the admin module from Django
from .models import SleepEssentials  # Import the SleepEssentials model from the current app's models file
from .forms import SleepEssentialsForm  # Import the custom form class for SleepEssentials


# Define a custom admin class for the SleepEssentials model
class SleepEssentialsAdmin(admin.ModelAdmin):
    form = SleepEssentialsForm  # Specify the form to use in the admin interface


# Register the SleepEssentials model with the custom admin class
admin.site.register(SleepEssentials, SleepEssentialsAdmin)
