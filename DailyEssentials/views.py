from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import DailyEssentials  # Import the DailyEssentials model from the current app


def daily_essentials_view(request):
    # Initialize context with an empty 'daily_essentials' list
    context = {
        'daily_essentials': [],
    }

    try:
        # Retrieve all daily essentials from the database
        daily_essentials = DailyEssentials.objects.all()

        # Update the context with the retrieved daily essentials
        context['daily_essentials'] = daily_essentials

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'themes_html/themes.html' template with the context
    return render(request, 'daily_essentials_html/daily_essentials.html', context)
