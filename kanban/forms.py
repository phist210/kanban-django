from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'status', 'priority']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': '#wrapper-content.backlog', 'required': True, 'placeholder': 'Task...'}
            ),
            'status': forms.Select(
                attrs={'id': '#wrapper-content.backlog', 'required': True},
                choices=(('Backlog', 'Backlog'), ('Active', 'Active'), ('Complete', 'Complete'))
            ),
            'priority': forms.Select(
                attrs={'id': '#wrapper-content.backlog', 'required': True, 'placeholder': '1-10...'},
                choices=(('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10))
            ),
        }
