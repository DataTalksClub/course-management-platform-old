from allauth.account.forms import LoginForm
from django import forms


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type':'email','id':'floating-input','class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class':'form-check-input'})
        
        self.fields['login'].label = ''
        self.fields['password'].label = ''