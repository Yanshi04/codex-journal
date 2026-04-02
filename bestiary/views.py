from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .forms import MonsterForm
from .models import Monster
import csv
from django.http import HttpResponse
from .tasks import send_witcher_notification
# from profiles.models import Profile
# from django.shortcuts import render, redirect, get_object_or_404

class ShowAllMonsters(LoginRequiredMixin, ListView):
    model = Monster
    template_name = 'bestiary/bestiary_list.html'
    context_object_name = 'monsters'

    def get_queryset(self):
        all_beasts = Monster.objects.filter(hunter=self.request.user.profile)
        user_choice = self.request.GET.get('sort')

        search_word = self.request.GET.get('search_word')

        if search_word:
            all_beasts = all_beasts.filter(monster_name__icontains =search_word)

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
        context['search_word'] = self.request.GET.get('search_word', '')
        return context


class CreateMonsterPage(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Monster
    form_class = MonsterForm
    template_name = 'bestiary/monster_create.html'
    success_url = reverse_lazy('bestiary_list')
    permission_required = 'bestiary.add_monster'

    def form_valid(self, form):
        form.instance.hunter = self.request.user.profile
        response = super().form_valid(form)
        send_witcher_notification.delay(
            hunter_name=self.request.user.username,
            monster_name=self.object.monster_name
        )
        return response


class MonsterDetailsPage(LoginRequiredMixin, DetailView):
    model = Monster
    template_name = 'bestiary/monster_details.html'

    def get_queryset(self):
        return Monster.objects.filter(hunter=self.request.user.profile)

class EditMonsterPage(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Monster
    form_class = MonsterForm
    template_name = 'bestiary/monster_edit.html'
    permission_required = 'bestiary.change_monster'

    def get_success_url(self):
        return reverse_lazy('monster_details', kwargs={'pk': self.object.pk})

    def get_queryset(self):  # Isolated
        return Monster.objects.filter(hunter=self.request.user.profile)

class DeleteMonsterPage(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Monster
    template_name = 'bestiary/monster_confirm_delete.html'
    success_url = reverse_lazy('bestiary_list')
    permission_required = 'bestiary.delete_monster'

    def get_queryset(self):  # Isolated
        return Monster.objects.filter(hunter=self.request.user.profile)


class DownloadCSVView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="my_codex_records.csv"'
        writer = csv.writer(response)
        writer.writerow(['Beast Name', 'Classification', 'Danger Level', 'Hunter Notes'])
        all_beasts = Monster.objects.filter(hunter = self.request.user.profile)

        for beast in all_beasts:
            name = beast.monster_name
            group = beast.kind.group_name
            danger = beast.get_level_of_danger_display()
            notes = beast.my_notes

            current_row = [name, group, danger, notes]
            writer.writerow(current_row)

        return response