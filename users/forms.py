from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
	username = forms.CharField(label="Utilisateur", widget=forms.TextInput(attrs={
		'placeholder': "Email ou Nom d'utilisateur",
		}))
	password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
		'placeholder': "Mot de passe",
		}))


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']