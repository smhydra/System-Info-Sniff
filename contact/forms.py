from django import forms
from .models import TextUpload

class TextUploadForm(forms.ModelForm):
    class Meta:
        model = TextUpload
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter title for your text'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Paste your long paragraph or text here...',
                'rows': 10
            }),
        }
