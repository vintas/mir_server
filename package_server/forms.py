from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Package, Library

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'version', 'description','version', 'libraries', 'file', 'dependencies']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'libraries': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': True}),
            'dependencies': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'shell_script': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    # Adding read-only date_added field for display purposes
    date_added = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'version', 'file', 'dependencies']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': True}),
            'dependencies': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
