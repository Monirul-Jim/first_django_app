from typing import Any
from django import forms
from django.core import validators


class TeachersRegistration(forms.Form):
    first_name = forms.CharField(
        label="Enter your first name", label_suffix=' ')
    last_name = forms.CharField(
        label="Enter your last name",   widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    email = forms.EmailField(label="Enter your email", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)

    def clean(self):
        cleaned_data = super().clean()
        right_Pass = self.cleaned_data['password']
        wrong_Pass = self.cleaned_data['re_password']
        if right_Pass != wrong_Pass:
            raise forms.ValidationError("Password does not match")
