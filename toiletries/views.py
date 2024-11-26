from django.shortcuts import render
from django.contrib import messages
from .models import Toiletries

def toiletries_view(request):
    context = {
        'toiletries': [],
    }

    try:
        toiletries = Toiletries.objects.all()
        context['toiletries'] = toiletries
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'toiletries_html/toiletries.html', context) 