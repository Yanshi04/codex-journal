# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Quest
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import QuestForm


class QuestListView(LoginRequiredMixin, ListView):
    model = Quest
    template_name = 'quests/quest_list.html'
    context_object_name = 'quests'

    def get_queryset(self):
        return Quest.objects.filter(profile=self.request.user.profile)


class QuestCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Quest
    form_class = QuestForm
    template_name = 'quests/quest_create.html'
    success_url = reverse_lazy('quest_list')
    permission_required = 'quests.add_quest'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

class QuestEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Quest
    form_class = QuestForm
    template_name = 'quests/quest_edit.html'

    success_url = reverse_lazy('quest_list')
    permission_required = 'quests.change_quest'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs

    def get_queryset(self):
        return Quest.objects.filter(profile=self.request.user.profile)

class QuestDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Quest
    template_name = 'quests/quest_confirm_delete.html'
    success_url = reverse_lazy('quest_list')
    permission_required = 'quests.delete_quest'

    def get_queryset(self):
        return Quest.objects.filter(profile=self.request.user.profile)