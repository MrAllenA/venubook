from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from django.template.defaulttags import comment

from .models import Persons


class NameForm(forms.ModelForm):
    # your_name = forms.CharField(label='Username', max_length=100)
    class Meta:
        model = Persons
        fields = ('name', 'pasn')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'pasn': Pass
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),



        }
