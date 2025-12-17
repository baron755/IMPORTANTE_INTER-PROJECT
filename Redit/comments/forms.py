from django import forms 
from .models import Announcement

class PostForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'context']
        
class CommentForms(forms.ModelForm):
    class Meta:
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'rows':3,'placeholder': "Ваш коментар..."})}