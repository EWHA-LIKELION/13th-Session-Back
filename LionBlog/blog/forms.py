from django import forms
from .models import Post, Comment

class Postform(forms.ModelForm):
  #Modelform: model과 field를 지정하면 자동으로 form을 만들어줌
  class Meta:
    model=Post
    fields=['title','body','photo']

class Commentform(forms.ModelForm):
  class Meta:
    model=Comment
    fields=['username', 'comment_text']