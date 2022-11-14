from django.contrib.auth.models import User
from auth_app.models import UserProfileInfo
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
