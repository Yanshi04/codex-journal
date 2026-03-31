# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Quest
from profiles.models import Profile


class QuestListView(ListView):
    model = Quest
    template_name = 'quests/quest_list.html'
    context_object_name = 'quests'


class QuestCreateView(CreateView):
    model = Quest
    template_name = 'quests/quest_create.html'
    fields = ['title', 'description', 'monsters', 'is_completed']
    success_url = reverse_lazy('quest_list')

    def form_valid(self, form):
        form.instance.profile = Profile.objects.first()
        return super().form_valid(form)

class QuestEditView(UpdateView):
    model = Quest
    template_name = 'quests/quest_edit.html'
    fields = ['title', 'description', 'monsters', 'is_completed']
    success_url = reverse_lazy('quest_list')

class QuestDeleteView(DeleteView):
    model = Quest
    template_name = 'quests/quest_confirm_delete.html'
    success_url = reverse_lazy('quest_list')
