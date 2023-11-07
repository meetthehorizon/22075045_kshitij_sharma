from .models import ShortURL
from django import forms

class createNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields ={'long_url'}
        widgets = {
            'long_url': forms.TextInput()
        }