from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import FeedingSupplies  # Import the FeedingSupplies model from the current app


def feeding_supplies_view(request):
    # Initialize context with an empty 'feeding_supplies' list
    context = {
        'feeding_supplies': [],
    }

    try:
        # Retrieve all feeding supplies from the database
        feeding_supplies = FeedingSupplies.objects.all()

        # Update the context with the retrieved feeding supplies
        context['feeding_supplies'] = feeding_supplies

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'feeding_supplies_html/feeding_supplies.html' template with the context
    return render(request, 'feeding_supplies_html/feeding_supplies.html', context)
