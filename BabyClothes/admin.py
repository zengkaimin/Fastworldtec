from django.contrib import admin  # Import the admin module from Django
from .models import BabyClothes  # Import the BabyClothes model
from .forms import BabyClothesForm  # Import the BabyClothesForm


# Define a custom ModelAdmin class for the BabyClothes model
class BabyClothesAdmin(admin.ModelAdmin):
    # Specify the custom form to use in the admin interface
    form = BabyClothesForm
    

# Register the BabyClothes model with the custom BabyClothesAdmin class
admin.site.register(BabyClothes, BabyClothesAdmin)
