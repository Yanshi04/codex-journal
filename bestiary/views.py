from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import MonsterForm
from .models import Monster
# from profiles.models import Profile
# from django.shortcuts import render, redirect, get_object_or_404

class ShowAllMonsters(ListView):
    model = Monster
    template_name = 'bestiary/bestiary_list.html'
    context_object_name = 'monsters'

    def get_queryset(self):
        all_beasts = Monster.objects.all()
        user_choice = self.request.GET.get('sort')
        if user_choice == 'name_desc':
            all_beasts = all_beasts.order_by('-monster_name')
        elif user_choice == 'danger':
            all_beasts = all_beasts.order_by('-level_of_danger')
        else:
            all_beasts = all_beasts.order_by('monster_name')
        return all_beasts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'name_asc')
        return context


class CreateMonsterPage(CreateView):
    model = Monster
    form_class = MonsterForm
    template_name = 'bestiary/monster_create.html'
    success_url = reverse_lazy('bestiary_list')

class MonsterDetailsPage(DetailView):
    model = Monster
    template_name = 'bestiary/monster_details.html'

class EditMonsterPage(UpdateView):
    model = Monster
    form_class = MonsterForm
    template_name = 'bestiary/monster_edit.html'

    def get_success_url(self):
        return reverse_lazy('monster_details', kwargs={'pk': self.object.pk})

class DeleteMonsterPage(DeleteView):
    model = Monster
    template_name = 'bestiary/monster_confirm_delete.html'
    success_url = reverse_lazy('bestiary_list')