from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Specify the model
        fields = '__all__'  # Include all fields from the model
