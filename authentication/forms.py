from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(maxlength=60, label="Nom d'utilisateur")
    password = forms.CharField(maxlenght=60, widget=forms.PasswordInput, label="Mot de passe")