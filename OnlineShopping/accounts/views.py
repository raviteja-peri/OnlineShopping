from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUp(CreateView):
    form_class=RegistrationForm
    success_url=reverse_lazy('accounts:login')
    template_name='accounts/register_form.html'
