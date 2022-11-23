from allauth.account.forms import LoginForm, SignupForm
from django import forms


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type':'email','id':'floating-input','class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class':'form-check-input'})
        
        self.fields['login'].label = ''
        self.fields['password'].label = ''

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'type':'email','id':'floating-input','class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Password(again)'})

        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''