from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import WeaponForm, WeaponSearchForm
from .models import Weapon

class WeaponListView(ListView):
    model = Weapon
    template_name = 'armory/weapon_list.html'
    context_object_name = 'weapons'

    def get_queryset(self):
        queryset = super().get_queryset()

        search_word = self.request.GET.get('search_word')
        sort_option = self.request.GET.get('sort', 'name_asc')
        if search_word:
            queryset = queryset.filter(name__icontains=search_word)


        if sort_option == 'name_desc':
            queryset = queryset.order_by('-name')
        elif sort_option == 'damage_desc':
            queryset = queryset.order_by('-damage')
        else:
            queryset = queryset.order_by('name')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = WeaponSearchForm(self.request.GET)
        context['search_word'] = self.request.GET.get('search_word', '')
        context['current_sort'] = self.request.GET.get('sort', 'name_asc')
        return context

class WeaponCreateView(LoginRequiredMixin, CreateView):
    model = Weapon
    form_class = WeaponForm
    template_name = 'armory/weapon_form.html'
    success_url = reverse_lazy('weapon_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class WeaponUpdateView(LoginRequiredMixin, UpdateView):
    model = Weapon

    form_class = WeaponForm
    template_name = 'armory/weapon_form.html'
    success_url = reverse_lazy('weapon_list')

class WeaponDeleteView(LoginRequiredMixin, DeleteView):
    model = Weapon

    template_name = 'armory/weapon_confirm_delete.html'
    success_url = reverse_lazy('weapon_list')