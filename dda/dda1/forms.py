from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.template.defaulttags import comment

from .models import Persons, reg


class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['pasn'].required = False

    class Meta:
        model = Persons
        fields = ('name', 'pasn')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'pasn': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
            }),

        }


class RegForm(forms.ModelForm):
    class Meta:
        model = reg
        fields = ('name', 'pasn1', 'pasn2', 'email')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'pasn1': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
            }),
            'pasn2': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 're-type password'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'example@gmail.com'
            }),
        }
