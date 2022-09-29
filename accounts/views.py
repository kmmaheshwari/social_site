from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm


# Create your views here.
class Signup(CreateView):
    form_class=SignupForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
