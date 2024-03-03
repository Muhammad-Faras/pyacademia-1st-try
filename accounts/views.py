
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from .forms import Login_Auth_Form
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUser_Form

class LoginAuthView(LoginView):
    form_class = Login_Auth_Form
    success_url = reverse_lazy('feed')
    
class SignupView(CreateView):
    form_class = CustomUser_Form
    template_name='registration/signup.html'
    success_url = reverse_lazy('login')
    
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('feed')