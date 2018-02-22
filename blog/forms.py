from django import forms
from . import models
class CreateArtcile(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'text', 'thumbnail']
