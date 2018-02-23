from django import forms
from . import models
class CreateArtcile(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'text', 'thumbnail']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
