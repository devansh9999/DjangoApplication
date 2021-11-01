from django import forms

class Login_Form(forms.Form):
    Username=forms.CharField(max_length=50)
    Password=forms.CharField(widget=forms.PasswordInput)