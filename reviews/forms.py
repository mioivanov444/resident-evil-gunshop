from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'rating']
        labels = {
            'name': 'Your name (optional)',
            'text': 'Review',
            'rating': 'Rating (1-5)',
        }
        help_texts = {
            'rating': 'Enter a number from 1 to 5',
        }