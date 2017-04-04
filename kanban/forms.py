from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
<<<<<<< HEAD
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
=======
        fields = ('name', 'status', 'priority',)

    def in_range(priority):
        if priority not in range(1, 11):
            raise forms.ValidationError('This field must '
                                        'be an integer 1-10.')


class EditTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'status', 'priority',)

    def in_range(priority):
        if priority not in range(1, 11):
            raise forms.ValidationError('This field must '
                                        'be an integer 1-10.')
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed
