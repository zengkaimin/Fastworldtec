from django.contrib import admin  # Import the admin module from Django
from .models import FeedingSupplies  # Import the FeedingSupplies model
from .forms import FeedingSuppliesForm  # Import the FeedingSuppliesForm


# Define a custom ModelAdmin class for the FeedingSupplies model
class FeedingSuppliesAdmin(admin.ModelAdmin):
    # Specify the custom form to use in the admin interface
    form = FeedingSuppliesForm


# Register the FeedingSupplies model with the custom FeedingSuppliesAdmin class
admin.site.register(FeedingSupplies, FeedingSuppliesAdmin)
