from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'bio']

        widgets = {
            'first_name': forms.TextInput(attrs = {'placeholder': 'Please input your first name'}),
            'last_name': forms.TextInput(attrs = {'placeholder': 'Please input your last name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Tell your story...', 'rows': 3}),

        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name[0].isupper():
            raise forms.ValidationError("The name must start with a capital letter. Please make sure that is the case.")
        return first_name
