from django.contrib import admin  # Import the admin module from Django
from .models import LargeItems  # Import the LargeItems model from the current app's models file
from .forms import LargeItemsForm  # Import the custom form class for LargeItems


# Define a custom admin class for the LargeItems model
class LargeItemsAdmin(admin.ModelAdmin):
    form = LargeItemsForm  # Specify the form to use in the admin interface


# Register the LargeItems model with the custom admin class
admin.site.register(LargeItems, LargeItemsAdmin)
