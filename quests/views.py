# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Quest
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestForm


class QuestListView(ListView):
    model = Quest
    template_name = 'quests/quest_list.html'
    context_object_name = 'quests'


class QuestCreateView(LoginRequiredMixin, CreateView):
    model = Quest
    form_class = QuestForm
    template_name = 'quests/quest_create.html'
    success_url = reverse_lazy('quest_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

class QuestEditView(LoginRequiredMixin, UpdateView):
    model = Quest
    form_class = QuestForm
    template_name = 'quests/quest_edit.html'

    success_url = reverse_lazy('quest_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs

class QuestDeleteView(LoginRequiredMixin, DeleteView):
    model = Quest
    template_name = 'quests/quest_confirm_delete.html'
    success_url = reverse_lazy('quest_list')
