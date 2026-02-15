from django import forms
from .models import Gun, Category

class GunForm(forms.ModelForm):
    class Meta:
        model = Gun

        fields = ['name', 'game', 'real_life_name', 'description', 'categories']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter gun name'
                }),

            'game': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Game appearance'
                }),

            'real_life_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Real-world equivalent'
                }),

            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Enter description...'
                }),

            'categories': forms.CheckboxSelectMultiple(),
        }

        labels = {
            'real_life_name': 'Real-Life Counterpart',
        }

        help_texts = {
            'categories': 'Select one or more categories for this gun.',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Gun must have a name!")
        return name
