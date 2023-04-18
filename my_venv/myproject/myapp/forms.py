from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
      username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
      password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

      class Meta:
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
    
        fields = ['username', 'email', 'password1', 'password2']

          