from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

# 2. Login
class LoginUserView(LoginView):
    template_name = 'accounts/login.html'


# 3. Logout
class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')
