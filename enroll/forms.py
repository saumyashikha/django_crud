from django.core import validators
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['name', 'email', 'password']
    widgets = {
        'name': forms.TextInput(attrs={'class':'form-control','class':'form-group'}),
        'email': forms.EmailInput(attrs={'class':'form-control','class':'form-group'}),
        'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control','class':'form-group'}),
    }
