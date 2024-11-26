from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import BabyClothes  # Import the BabyClothes model from the current app


def baby_clothes_view(request):
    # Initialize context with an empty 'courses' list
    context = {
        'baby_clothes': [],
    }

    try:
        # Retrieve all baby clothes from the database
        baby_clothes = BabyClothes.objects.all()

        # Update the context with the retrieved baby clothes
        context['baby_clothes'] = baby_clothes

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'baby_clothes_html/baby_clothes.html' template with the context
    return render(request, 'baby_clothes_html/baby_clothes.html', context)
