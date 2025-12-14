from django import forms 
from .models import Announcement

class NoteForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'context']