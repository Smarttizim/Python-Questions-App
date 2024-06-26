# forms.py

from django import forms
from .models import Contact

class ContactFileForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['file']
