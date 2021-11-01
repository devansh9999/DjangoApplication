from django import forms
from django.shortcuts import render
from django.contrib.auth.views import LoginView

from auth.forms import Login_Form

# from django.contrib.auth.decorators import login_required

# Create your views here.
class Login(LoginView):
    template_name='Login.html'
    LoginForm=Login_Form
    redirect_authenticated_user=True
    success_url="/"

def Home(request):
    return render(request,"index.html")
    
