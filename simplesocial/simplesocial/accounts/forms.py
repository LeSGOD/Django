from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(forms.ModelForm):
    """Form definition for UserCreate."""

    class Meta:
        """Meta definition for UserCreateform."""

        model = get_user_model
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Adress'
