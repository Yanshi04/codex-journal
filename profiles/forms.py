from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'bio', 'profile_picture']

        labels = {
            'first_name': 'Given Name',
            'last_name': 'Family Name',
            'profile_pic': 'Hunter Portrait URL',
            'bio': 'The Witcher\'s Tale',
        }

        help_texts = {
            'email': 'This email is linked to your account and cannot be changed here.',
            'profile_pic': 'Provide a link to an image of your hunter.',
        }


        widgets = {
            'first_name': forms.TextInput(attrs = {'placeholder': 'Please input your first name'}),
            'last_name': forms.TextInput(attrs = {'placeholder': 'Please input your last name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Tell us your story...', 'rows': 3}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name[0].isupper():
            raise forms.ValidationError("The name must start with a capital letter. Please make sure that is the case.")
        return first_name
