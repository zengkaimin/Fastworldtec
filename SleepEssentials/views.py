from django.shortcuts import render
from django.contrib import messages
from .models import SleepEssentials

def sleep_essentials_view(request):
    context = {
        'sleep_essentials': [],
    }

    try:
        sleep_essentials = SleepEssentials.objects.all()
        context['sleep_essentials'] = sleep_essentials
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'sleep_essentials_html/sleep_essentials.html', context) 