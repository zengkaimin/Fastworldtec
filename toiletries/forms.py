from django import forms
from .models import Toiletries
from mdeditor.fields import MDTextFormField

class ToiletriesForm(forms.ModelForm):
    description = MDTextFormField()
    
    class Meta:
        model = Toiletries
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            model_field = self._meta.model._meta.get_field(field_name)