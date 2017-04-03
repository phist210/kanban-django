from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
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
