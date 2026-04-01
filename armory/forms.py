from django import forms
from .models import Weapon

class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'damage', 'description']

        labels = {
            'name': 'Name',
            'damage': 'Base Attack Power',
            'description': 'Details',
        }

        help_texts = {
            'damage': 'A witcher\'s blade must be sharp.Minimum 10 damage required.',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'for example, Silver Sword of the Griffin'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the steel or silver quality...', 'rows': 3}),
        }

    def clean_damage(self):
        damage = self.cleaned_data.get('damage')

        if damage < 10:
            raise forms.ValidationError("Even a blunt butter knife does more than 9 damage! Sharpen your weapon.")
        return damage


class WeaponSearchForm(forms.Form):
    search_word = forms.CharField(
        required=False,
        label='Search Armory',
        widget=forms.TextInput(attrs={'placeholder': 'Search by name...'})
    )