from rest_framework import serializers
from blog.models import Post, LANGUAGE_CHOICES, Comment


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ["id", 'post', 'username', 'comment_text', 'created_at']

class PostSerializer(serializers.ModelSerializer):
  comment = CommentSerializer(many = True, read_only= True)
  
  class Meta:
    model = Post
    fields = ['id', 'title', 'date', 'body', 'language']

