from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
# from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from Java import models




# Create your views here.
# def Home(request):
#     return render(request,"index.html")

class logout(LogoutView):
    pass

class Questions(LoginRequiredMixin, ListView):
    login_url="/Login"
    model=models.AddData
    template_name="Questions.html"
    context_object_name="Quests"

class ADD_DATA(LoginRequiredMixin,CreateView):
    login_url="/Login"
    model=models.AddData
    template_name='Add_Data.html'
    fields="__all__"
    success_url="/Questions#test1"

# class Login(FormView):
#     template_name='Login.html'
#     form_class=LoginForm
#     success_url="/"
#     context_object_name="Form"

class Notes(LoginRequiredMixin,CreateView):
    login_url="/Login"
    model=models.Notes
    template_name='Notes.html'
    fields="__all__"
    success_url="/Java/Questions/Notes"

class NotesView(LoginRequiredMixin,ListView):
    login_url="/Login"
    model=models.Notes
    template_name="NotesView.html"
    context_object_name="imgs"
