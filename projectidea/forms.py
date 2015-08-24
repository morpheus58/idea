__author__ = 'Morya Jr'
from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'idea', 'created_at', 'category')