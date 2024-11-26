from django import forms
from .models import Toiletries

class ToiletriesForm(forms.ModelForm):
    class Meta:
        model = Toiletries
        fields = '__all__' 