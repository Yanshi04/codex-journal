# from django.shortcuts import render, redirect
# from .forms import ProfileCreateForm
# from .models import Profile
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileCreateForm
from bestiary.models import Monster

class MakeProfile(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('home')

class ViewMyProfile(DetailView):
    template_name = 'profiles/profile-details.html'
    def get_object(self, queryset=None):
        my_profile = Profile.objects.first()
        return my_profile

class ChangeMyProfile(UpdateView):
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        my_profile = Profile.objects.first()
        return my_profile

class RemoveMyProfile(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        my_profile = Profile.objects.first()
        return my_profile

    def form_valid(self, form):
        Monster.objects.all().delete()
        return super().form_valid(form)