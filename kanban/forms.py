from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = ['name', 'description', 'status']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': '.wrapper-content', 'required': True, 'placeholder': '>'}
            ),
            'description': forms.TextInput(
                attrs={'id': '.wrapper-content', 'required': False, 'placeholder': '>'}
            ),
            'status': forms.Select(
                attrs={'id': '.wrapper-content', 'required': True},
                choices=(('Backlog', 'Backlog'), ('Active', 'Active'), ('Complete', 'Complete'))
            ),
        }
