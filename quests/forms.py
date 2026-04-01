from django import forms

from bestiary.models import Monster
from .models import Quest


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['title', 'description', 'monsters', 'is_completed']
        labels = {
            'is_completed': 'Quest Finished?',
            'monsters': 'Monsters Involved',
        }
        help_texts = {
            'description': 'Provide the details of the contract as seen on the notice board.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'E.g. The Beast of White Orchard'}),
            'description': forms.Textarea(attrs={'placeholder': 'A griffin is terrorizing the roads...'}),
        }

    # quests/forms.py

    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('profile', None)
        super().__init__(*args, **kwargs)

        if profile:
            from bestiary.models import Monster
            self.fields['monsters'].queryset = Monster.objects.filter(hunter=profile)

        if self.instance and self.instance.pk:
            self.fields['title'].disabled = True
            self.fields['title'].help_text = "Contracts are binding. The title cannot be changed."