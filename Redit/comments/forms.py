from django import forms 
from .models import Announcement

class PostForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'context']