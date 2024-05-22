from django import forms
from .models import  GamePost

class GamePostForm(forms.ModelForm):
    class Meta:
        model = GamePost
        fields = [
            'header',
            'text',
            'CategoryCheck',
        ]