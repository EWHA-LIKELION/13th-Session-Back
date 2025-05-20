from django import forms
from .models import Post, Comment

class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'body', 'photo']

class Commentform(forms.ModelForm):
    class Meta:

        model=Comment
        fields=['username', 'comment_text']