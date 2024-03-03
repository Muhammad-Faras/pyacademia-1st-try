from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser_Model

class CustomUser_Form(UserCreationForm):
    class Meta:
        model = CustomUser_Model
        fields = ('username', 'first_name', 'last_name', 'email', 'university', 'skills')
    
















class Login_Auth_Form(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom HTML attributes to the username field
        self.fields['username'].widget.attrs.update({
            'class': 'custom-class',
            'id': 'username-id',
            'name': 'custom-username-name',
            'placeholder': 'Enter your username',
            # Add more attributes as needed
        })
        self.fields['username'].label = "Username Label chabged"
        # Add custom HTML attributes to the password field
        self.fields['password'].widget.attrs.update({
            'class': 'custom-class',
            'id': 'password-id',
            'name': 'custom-password-name',
            'placeholder': 'Enter your password',
            # Add more attributes as needed
        })


