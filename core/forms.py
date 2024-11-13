# core/forms.py
from django import forms
from .models import Group
from django.contrib.auth import get_user_model  # Import to dynamically fetch custom user model

User = get_user_model()  # Use this to refer to core.User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User  # This now references core.User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'mentor', 'members']
