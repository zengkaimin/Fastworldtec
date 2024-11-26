from django.contrib import admin
from .models import Toiletries
from .forms import ToiletriesForm

class ToiletriesAdmin(admin.ModelAdmin):
    form = ToiletriesForm

admin.site.register(Toiletries, ToiletriesAdmin) 