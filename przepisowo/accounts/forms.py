from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control col-md-6'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control col-md-6'}))


class UserRegistrationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-6'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-6'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Podane hasła nie są identyczne')
        return cd['password2']
