from django import forms
from .models import Monster

class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'

        widgets = {'my_notes': forms.Textarea(attrs={'placeholder': 'Write your observations about the beast you encountered...'}),
        'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/monster.jpg'})}

class MonsterDeleteForm(MonsterForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'