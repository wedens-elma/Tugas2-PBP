from django.forms import ModelForm
from django import forms
from .models import Task

class Form(ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.TextInput()
    class Meta:
        model = Task
        fields = ['title', 'description']