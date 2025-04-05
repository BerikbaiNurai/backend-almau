from django import forms
from .models import Blog


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'author']
