from django import forms
from .models import Gun, Category

class GunForm(forms.ModelForm):
    class Meta:
        model = Gun
        fields = ['name', 'game', 'real_life_name', 'description', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'rows':4, 'cols':40}),
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
