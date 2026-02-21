from django import forms
from .models import Monster

class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'

        widgets = {'my_notes': forms.Textarea(attrs={'placeholder': 'Write your observations about the beast you encountered...'}),
        'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/monster.jpg'})}

class MonsterSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search by Name',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter monster name'})
    )