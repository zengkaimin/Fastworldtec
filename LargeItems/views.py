from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import LargeItems  # Import the LargeItems model from the current app


def large_items_view(request):
    # Initialize context with an empty 'large_items' list
    context = {
        'large_items': [],
    }

    try:
        # Retrieve all large items from the database
        large_items = LargeItems.objects.all()

        # Update the context with the retrieved large items
        context['large_items'] = large_items

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'large_items_html/large_items.html' template with the context
    return render(request, 'large_items_html/large_items.html', context)
