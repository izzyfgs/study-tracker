from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['subject', 'year', 'total_questions', 'score']
        widgets = {
            'subject': forms.Select(attrs={
                'class': 'form-control'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1978,
                'max': 2025
            }),
            'total_questions': forms.NumberInput(attrs={
                'class': 'form-control',
                'value': 50,
                'min': 1
            }),
            'score': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
        }
        labels = {
            'subject': 'Subject',
            'year': 'Year of Past Questions',
            'total_questions': 'Total Questions',
            'score': 'Score Obtained',
        }
